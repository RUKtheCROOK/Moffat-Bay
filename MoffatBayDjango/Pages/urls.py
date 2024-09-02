from django.urls import path
from .views import HomePageView #, AboutPageView **this is an example comment** to actually implement this the about view need to be uncommented and imported here. Then the url needs to be uncommented.

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('about/', AboutPageView.as_view(), name='about'),
]
