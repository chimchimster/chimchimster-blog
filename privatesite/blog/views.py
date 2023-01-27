from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Portfolio


def index(request):
    return render(request, 'blog/index.html')


def get_portfolio(request, portfolio_slug):
    portfolio = Portfolio.objects.filter(slug=portfolio_slug)
    print(portfolio)
    return render(request, 'blog/index.html', {
        'portfolio': portfolio,
    })