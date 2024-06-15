from django.urls import path
from .views import (DestinationListView, DestinationDetailView, DestinationCreateView, DestinationUpdateView, DestinationDeleteView,
                    DestinationListCreateAPIView, DestinationRetrieveUpdateDestroyAPIView)

urlpatterns = [
    # Django views for HTML templates
    path('', DestinationListView.as_view(), name='destination_list'),
    path('destination/<int:pk>/', DestinationDetailView.as_view(), name='destination_detail'),
    path('destination/new/', DestinationCreateView.as_view(), name='destination_create'),
    path('destination/<int:pk>/edit/', DestinationUpdateView.as_view(), name='destination_update'),
    path('destination/<int:pk>/delete/', DestinationDeleteView.as_view(), name='destination_delete'),

    # DRF views for API endpoints
    path('api/destinations/', DestinationListCreateAPIView.as_view(), name='destination_api_list_create'),
    path('api/destination/<int:pk>/', DestinationRetrieveUpdateDestroyAPIView.as_view(), name='destination_api_retrieve_update_destroy'),
]
