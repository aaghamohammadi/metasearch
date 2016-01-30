from elasticsearch import Elasticsearch
import os, json

es = Elasticsearch()


def index(elastic, dir):
    path_to_json = dir
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    for js in json_files:
        with open(os.path.join(path_to_json, js)) as json_file:
            data = json.loads(json_file)
            elastic.index(index='researchGate', doc_type='articles', body=data)
