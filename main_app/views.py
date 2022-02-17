from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from .models import Fish

# Create your views here.


class FishList(ListView):
    model = Fish


class FishCreate(CreateView):
    model = Fish
    fields = '__all__'
    success_url = '/'


class FishDelete(DeleteView):
    model = Fish
    success_url = '/'
