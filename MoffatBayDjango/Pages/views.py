from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

def navBar(request):
    return render(request, 'navbar.html')
# class AboutPageView(TemplateView):
#
#     template_name = 'about.html'