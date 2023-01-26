from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Portfolio

def index(request):
    return render(request, 'blog/index.html')

def get_portfolio(request, portfolio_slug):
    portfolio = Portfolio.objects.get(pk=1)
    return render(request, 'blog/index.html', {
        'portfolio': portfolio,
    })