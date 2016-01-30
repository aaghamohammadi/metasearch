from elasticsearch import Elasticsearch
import os, json
from global_functions import update_progress


es = Elasticsearch()

def index(elastic, dir):
    path_to_json = dir
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    for i, js in enumerate(json_files):
        with open(os.path.join(path_to_json, js)) as json_file:
            data = json.loads(json_file)
            elastic.index(index='researchGate', doc_type='articles', body=data)
        update_progress(i, json_files.__len__())

def search(elastic, query_in, boost={'author':1, 'title':1, 'abstract':1}):
    query = {
        "query":{
            "match":{
            }
        }
    }

    if 'title' not in boost.keys():
        boost['title'] = 1
    if 'author' not in boost.keys():
        boost['author'] = 1
    if 'abstract' not in boost.keys():
        boost['abstract'] = 1


    if 'title' in query_in.keys():
        query["query"]["match"]["title"] = { "query":query_in["title"], "boost": boost['title']}
    if 'author' in query_in.keys():
        query["query"]["match"]["author"] = { "query":query_in["author"], "boost": boost['author']}
    if 'abstract' in query_in.keys():
        query["query"]["match"]["abstract"] = { "query":query_in["abstract"], "boost": boost['abstract']}

    response = elastic.search(index="researchGate", doc_type="articles", body=query)

    


