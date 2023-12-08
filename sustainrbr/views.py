# these imports aren't being used might not need them remove later if so
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse



from django.shortcuts import render, redirect, get_object_or_404 

from django.views import generic
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import RegisterForm

class IndexView(generic.TemplateView):
  template_name = "views/index.html"

"""
class loginView(generic.TemplateView):
  template_name = "views/login.html"
"""

"""
class registerView(FormView):
  template_name = "views/register.html"
  form_class = RegisterForm

  # reverse_lazy allows us to call "login" as the success url
  # before it was rooting us to /register/login
  success_url = reverse_lazy("login")

  def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
    form.send_email()
    return super().form_valid(form)

"""


# done this as a function rather than a class because it's easier 
# i know this is probably bad practise to mix classes and functions but time is limited

def register(response):

  if response.method == "POST":
    form = RegisterForm(response.POST)
    if form.is_valid():
      form.save()
    return redirect("/login")
  
  else:
    form = RegisterForm()


  return render(response, "views/register.html", {"form":form})
