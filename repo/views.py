from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Snippet


# Create your views here.


class SnippetList(generic.ListView):
    queryset = Snippet.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class SnippetDetail(generic.DetailView):
    model = Snippet
    template_name = 'snippet_detail.html'
