from django.urls import path
from .views import ReservationListView, ReservationDetailView, ReservationCreateView, ReservationUpdateView, ReservationDeleteView, ReservationSummaryView, ReservationConfirmView, ReservationCancelView

urlpatterns = [
    path('', ReservationListView.as_view(), name='reservation-list'),
    path('<int:pk>/', ReservationDetailView.as_view(), name='reservation-detail'),
    path('new/', ReservationCreateView.as_view(), name='book'),
    path('<int:pk>/update/', ReservationUpdateView.as_view(), name='reservation-update'),
    path('<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation-delete'),
    path('<int:pk>/summary/', ReservationSummaryView.as_view(), name='reservation-summary'),
    path('<int:pk>/confirm/', ReservationConfirmView.as_view(), name='reservation-confirm'),
    path('<int:pk>/cancel/', ReservationCancelView.as_view(), name='reservation-cancel'),
]
