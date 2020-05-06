import os, json
from django.shortcuts import render

# Create your views here.
from sklearn.feature_extraction.text import CountVectorizer
from kmeans.kmeans import Kmeans
from searching.forms import CrawlerForm, IndexForm, ClusterForm, PageRankForm, QueryForm
import matplotlib.pyplot as plt
from crawler.scheduler import Scheduler
from elasticsearch import Elasticsearch
from elasticSearch import searcher
from page_rank import adjacent_matrix, page_rank

es = Elasticsearch

def index(request):
    template_name = 'index.html'
    if request.method == "POST":
        if "crawl-btn" in request.POST:
            crawler_form = CrawlerForm(request.POST)
            if crawler_form.is_valid():
                n_docs = crawler_form.cleaned_data['n_docs']
                in_degree = crawler_form.cleaned_data['in_degree']
                out_degree = crawler_form.cleaned_data['out_degree']
                starting_url = crawler_form.cleaned_data['starting_url']
                urls = [x.strip() for x in starting_url.split(',')]
                crawler = Scheduler(starting_url=urls, num=n_docs, in_degre=in_degree, out_degree=out_degree)
                crawler.crawl()
            else:
                return render(request, template_name, {'crawler_form': crawler_form})
        if "index-btn" in request.POST:
            index_form = IndexForm(request.POST)
            if index_form.is_valid():
                direction = index_form.cleaned_data['direction']
                print(direction)
                searcher.index(es, direction)

            else:
                return render(request, template_name, {'index_form', index_form})
        if "cluster-btn" in request.POST:
            cluster_form = ClusterForm(request.POST)
            if cluster_form.is_valid():
                path_to_json = cluster_form.cleaned_data['direction']
                titles = []
                json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
                for js in json_files:
                    with open(os.path.join(path_to_json, js)) as json_file:
                        data = json.load(json_file)
                        titles.append(data["title"])
                        json_file.close()
                vectorizer = CountVectorizer()
                vectors = vectorizer.fit_transform(titles).todense().tolist()
                kmeans = Kmeans(vectors)
                k_points = []
                j_points = []
                for i in range(len(vectors)):
                    k_points.append(i + 1)
                    j_points.append(kmeans.kmenas(i + 1))

                plt.plot(j_points, k_points)
                plt.show()
            else:
                return render(request, template_name, {'cluster_form': cluster_form})
        if "page-rank-btn" in request.POST:
            page_rank_form = PageRankForm(request.POST)
            if page_rank_form.is_valid():
                alpha = page_rank_form.cleaned_data['alpha']
                threshold = page_rank_form.cleaned_data['threshold']



            else:
                return render(request, template_name, {'page_rank_form': page_rank_form})
        if "query-btn" in request.POST:
            query_form = QueryForm(request.POST)
            if query_form.is_valid():
                cluster = query_form.cleaned_data['cluster']
                pagerank = query_form.cleaned_data['pagerank']
                query = query_form.cleaned_data['query']
            else:
                return render(request, template_name, {'query_form': query_form})

    else:
        query_form = QueryForm()
        page_rank_form = PageRankForm()
        cluster_form = ClusterForm()
        crawler_form = CrawlerForm()
        index_form = IndexForm()
        return render(request, template_name,
                      {'query_form': query_form, 'page_rank_form': page_rank_form, 'cluster_form': cluster_form,
                       'crawler_form': crawler_form,
                       'index_form': index_form})
