# entity_extraction_spaCy
SpaCy is an opensource library for Natural Language Processing, which is written in python and cython. It provides a major NLP
tasks such as text classification, NER-Named Entity Recognition, POS tagging etc. I have tried to understand how NER woks in
spacy and implemeted it.

Spacy provides a default deep learning model trained on lots of data. This model works quite well in most of the cases for well
defiend entities like time, money, person, location etc. This model can identify more than 20 entites from any text data. But
sometimes we need such a model that can identify custom entities defined by us. Spacy provides training for such custom entites.
So we can extend a default model to predict new custom entities after traning it with new data. We can also train totally new model which
will only extract a custom entities traind by us. In this project I am training a totally new model which can only able to predict
a new custom entities.

I am using this [entity_annotated_dataset](https://www.kaggle.com/abhinavwalia95/entity-annotated-corpus) for training a custom NER model.

You can find a detailed description of this project from this blog I wrote on medium.
