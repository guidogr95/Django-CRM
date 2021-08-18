from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
  context = {
    'name': 'Guido',
    'age': 25
  }
  return render(request, "leads/home_page.html", context)
