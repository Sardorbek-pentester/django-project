from django.shortcuts import render
from django.views.generic import ListView,CreateView, UpdateView, DetailView, TemplateView
from .models import Projects

# Create your views here.

class FreeAudit(CreateView):
    model=Projects
    template_name='free_audit.html'
    fields=["project_name", "title", "author","about", "date_manufactured"]
    
class EditInfo(UpdateView):
    model=Projects
    template_name='edit.html'
    fields=["project_name", "title", "author","about", "date_manufactured"]

class DatailView(DetailView):
    model=Projects
    template_name='datail.html'
    
class HomePageView(TemplateView):
    template_name='home.html'
    
class AboutPageView(ListView):
    model=Projects
    template_name='about_us.html'
    
class BlogPageView(TemplateView):
    template_name='blog.html'
    
class ContentCreation(TemplateView):
    template_name='content_creation.html'
    
class ContentStrategy(TemplateView):
    template_name='content_strategy.html'