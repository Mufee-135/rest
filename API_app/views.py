

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Destination

class DestinationListView(ListView):
    model = Destination
    template_name = 'destination_list.html'

class DestinationDetailView(DetailView):
    model = Destination
    template_name = 'destination_detail.html'

class DestinationCreateView(CreateView):
    model = Destination
    template_name = 'destination_form.html'
    fields = ['name', 'state', 'district', 'description']
    success_url = reverse_lazy('destination_list')

class DestinationUpdateView(UpdateView):
    model = Destination
    template_name = 'destination_form.html'
    fields = ['name', 'state', 'district', 'description']
    success_url = reverse_lazy('destination_list')

class DestinationDeleteView(DeleteView):
    model = Destination
    template_name = 'destination_delete.html'
    success_url = reverse_lazy('destination_list')
# destinations/views.py

from rest_framework import generics
from .models import Destination
from .serializers import DestinationSerializer

class DestinationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
