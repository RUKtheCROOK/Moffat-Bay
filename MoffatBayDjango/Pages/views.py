from django.shortcuts import render
from django.views.generic import TemplateView

# Group Names: Taylor Mommer, John Garcia, Andrew Bach, Somsak Bounchareune, Torren Davis

# This is the view for the home page. It is a TemplateView that uses the home.html template.
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_type'] = 'home'
        return context

# This is the view for the about page. It is a TemplateView that uses the about.html template.
class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_type'] = 'about'
        return context

# This is the view for the attractions page. It is a TemplateView that uses the attractions.html template.
class AttractionsPageView(TemplateView):
    template_name = 'attractions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_type'] = 'attractions'
        return context

# We will not be using any of the following views in our project as of 9/24/2024:
# class BookPageView(TemplateView):
#     template_name = 'book.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['page_type'] = 'book'
#         return context

# class ContactPageView(TemplateView):
#     template_name = 'contact.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['page_type'] = 'contact'
#         return context

# class AboutPageView(TemplateView):
#
#     template_name = 'about.html'