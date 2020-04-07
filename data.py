import pandas as pd
import json


def processing(path_to_data):
    data = pd.read_csv(path_to_data, encoding='unicode_escape')
    d_length = len(data)
    p_data = []
    i = 0
    tag_set = set([])
    while i != d_length:
        text = ""
        entities = {}
        words_count = 0
        t_word_length = 0
        entity_list = []
        while 1:
            if data['Tag'][i] != 'O':
                start_pos = t_word_length + words_count
                tag = data['Tag'][i][2:]
                tag_set.add(tag)
                words_count += 1
                t_word_length += len(data['Word'][i])
                text += data['Word'][i] + " "
                i += 1
                while data['Tag'][i][0] not in {'B', 'O'}:
                    words_count += 1
                    t_word_length += len(data['Word'][i])
                    text += data['Word'][i] + " "
                    i += 1
                end_pos = t_word_length + words_count - 1
                entity_list.append((start_pos, end_pos, tag))
            else:
                words_count += 1
                t_word_length += len(data['Word'][i])
                text += data['Word'][i] + " "
                i += 1
            if i == d_length or isinstance(data['Sentence #'][i], str):
                break
        entities['entities'] = entity_list
        p_data.append((text.strip(), entities))
    tag_set = list(tag_set)
    whole_data = {"training_data": p_data, "tag_set": tag_set}
    with open('data_spacy_format/traning_data.json', 'w') as f:
        json.dump(whole_data, f, indent=4)
    return "Data_Generation_Process_is_Completed"
