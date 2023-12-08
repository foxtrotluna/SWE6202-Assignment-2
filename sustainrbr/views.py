from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

class IndexView(generic.TemplateView):
  template_name = "views/index.html"

class loginView(generic.TemplateView):
  template_name = "views/login.html"

class registerView(generic.TemplateView):
  template_name = "views/register.html"