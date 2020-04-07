import spacy
from spacy.util import compounding, minibatch
import random
from pathlib import Path
import json

data_spacy = open("data_spacy_format/traning_data.json").read()
data_spacy_json = json.loads(data_spacy)
training_data = data_spacy_json['training_data']
tag_set = data_spacy_json['tag_set']


def training_spacy_ner(n_iter=100, output_dir=None, new_model_name=None, model=None):
    if model is not None:
        nlp = spacy.load(model)
    else:
        nlp = spacy.blank('en')

    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner)
    else:
        ner = nlp.get_pipe('ner')

    for tag in tag_set:
        ner.add_label(tag)

    if model is None:
        optimizer = nlp.begin_training()
    else:
        optimizer = nlp.resume_training()

    size = compounding(4., 32., 1.001)
    print("hi")
    for it in range(n_iter):
        random.shuffle(training_data)
        batches = minibatch(training_data, size)
        losses = {}
        for batch in batches:
            texts, annots = zip(*batch)
            nlp.update(texts, annots, sgd=optimizer, losses=losses, drop=0.4)
        print(losses)

    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = new_model_name
        nlp.to_disk(output_dir)
        print("model is saved")


training_spacy_ner(output_dir="model", new_model_name="first_model", model=None)
