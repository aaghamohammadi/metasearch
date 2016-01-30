from django import forms
from searching.models import Crawler, Indexing


class CrawlerForm(forms.ModelForm):
    class Meta:
        model = Crawler
        fields = '__all__'


class IndexForm(forms.ModelForm):
    class Meta:
        model = Indexing
        fields = '__all__'
