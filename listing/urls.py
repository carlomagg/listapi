from django.urls import path
from .views import PropertyListingView

app_name = 'listing'

urlpatterns = [
    path('property-listings/', PropertyListingView.as_view(), name='property-listings'),
]
