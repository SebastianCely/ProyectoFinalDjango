from django.shortcuts import render
from django.views import generic


def render_index_view(request):
    return render(request, 'index.html')
