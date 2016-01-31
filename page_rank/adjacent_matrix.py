import json
import numpy as np
import re
import os
from pprint import pprint


def create_matrix(dir='./resources/jsons'):

    jsonss =[]
    path_to_json = dir
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    for i, js in enumerate(json_files):
        with open(os.path.join(path_to_json, js)) as json_file:
            jsonss.append(json.load(json_file))

    print(jsonss.__len__())

    uid_to_index = {}
    for i, jso in enumerate(jsonss):
        uid_to_index[jso['uid']] = i


    GT = np.zeros((jsonss.__len__(), jsonss.__len__()))

    for i, jso in enumerate(jsonss):
        for link in jso['in_links']:
            link_uid = re.search(r'\d+', link).group()
            if link_uid in uid_to_index.keys():
                print (jso['uid'])
                print(link_uid)
                GT[i][uid_to_index[link_uid]] = 1


        for link in jso['out_links']:
            link_uid = re.search(r'\d+', link).group()
            if link_uid in uid_to_index.keys():
                print (jso['uid'])
                print(link_uid)
                GT[i][uid_to_index[link_uid]] = 1
    pprint (GT)
    return (GT, uid_to_index)
