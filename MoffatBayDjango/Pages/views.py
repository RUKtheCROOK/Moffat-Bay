from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class AttractionsPageView(TemplateView):
    template_name = 'attractions.html'

class BookPageView(TemplateView):
    template_name = 'book.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

# class AboutPageView(TemplateView):
#
#     template_name = 'about.html'