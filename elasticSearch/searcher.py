from pprint import pprint

from elasticsearch import Elasticsearch
import os, json
from global_functions import update_progress
from operator import itemgetter



def index(elastic, dir='./resources/jsonFiles'):


    path_to_json = dir
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    for i, js in enumerate(json_files):

        with open(os.path.join(path_to_json, js)) as json_file:
            data = json.load(json_file)
            a = elastic.index(index='researchgate',  doc_type='articles', id=i,  body=data)

        update_progress(i, json_files.__len__())

def search(elastic, query_in, boost={'author':1, 'title':1, 'abstract':1}, num=6):
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

    response = elastic.search(index="researchgate", doc_type="articles", body=query)

    pprint(response)

    ans=[]

    for i,res in enumerate(response['hits']['hits']):
        ans.append((res['_source']['uid'], res['_source']['title'], res['_score']))


    return ans

def pagerank_search(r, uid_to_index, elastic, query_in, boost={'author':1, 'title':1, 'abstract':1}, num=6):

    response = search(elastic, query_in, boost, num)
    anss = []
    for i, ans in enumerate(anss):
        ans = (response[i][0], response[i][1], r[uid_to_index[response[i][1]]] * 1.2 + response[i][2] * 5)

    anss = sorted(anss, key=itemgetter(2))

    return anss