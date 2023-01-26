from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/<slug:portfolio_slug>', views.get_portfolio, name='portfolio'),


]