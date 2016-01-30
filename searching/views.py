from django.shortcuts import render

# Create your views here.
from searching.forms import CrawlerForm, IndexForm


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
                pass
            return render(request, template_name, {'crawler_form': crawler_form})
        if "index-btn" in request.POST:
            index_form = IndexForm(request.POST)
            if index_form.is_valid():
                direction = index_form.cleaned_data['direction']

                pass
            return render(request, template_name, {'index_form', index_form})


    else:
        crawler_form = CrawlerForm()
        index_form = IndexForm()
        return render(request, template_name, {'crawler_form': crawler_form, 'index_form': index_form})
