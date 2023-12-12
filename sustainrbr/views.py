# these imports aren't being used might not need them remove later if so
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404 
from django.views import generic
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from chartjs.views.lines import BaseLineChartView

from .forms import RegisterForm

example_products = [
    {"name":"product A"},
    {"name":"product B"},
    {"name":"product C"},
    {"name":"product D"},
    {"name":"product E"},
    {"name":"product F"},
    {"name":"product G"},
    {"name":"product H"},
    {"name":"product I"},
    {"name":"product J"},
  ]

def index(response):
  return render(response,"views/index.html", {"recommended_products": example_products[:4]} )

def account(response):
  return render(response,"views/account/account.html")

def product(response,productid):
  return render(response,"views/products/product.html",{"productid":productid})

def products(response):
  return render(response,"views/products/products.html",{"products":example_products})

def charts(BaseLineChartView):
  return render("views/account/charts.html")

def register(response):
  if response.method == "POST":
    form = RegisterForm(response.POST)
    if form.is_valid():
      form.save()
    return redirect("/login")
  else:
    form = RegisterForm()

  return render(response, "views/registration/register.html", {"form":form})
