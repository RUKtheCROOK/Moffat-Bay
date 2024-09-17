from django.urls import path
from .views import HomePageView, AboutPageView, AttractionsPageView #, ContactPageView , BookPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('attractions/', AttractionsPageView.as_view(), name='attractions'),
    # path('book/', BookPageView.as_view(), name='book'),
    # path('contact/', ContactPageView.as_view(), name='contact'),
    # path('about/', AboutPageView.as_view(), name='about'),
]
