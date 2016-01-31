from django import forms
from searching.models import Crawler, Indexing, Clustering, PageRanking, Query


class CrawlerForm(forms.ModelForm):
    class Meta:
        model = Crawler
        fields = '__all__'


class IndexForm(forms.ModelForm):
    class Meta:
        model = Indexing
        fields = '__all__'


class ClusterForm(forms.ModelForm):
    class Meta:
        model = Clustering
        fields = '__all__'


class PageRankForm(forms.ModelForm):
    class Meta:
        model = PageRanking
        fields = '__all__'


class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = '__all__'
