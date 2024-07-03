from django.urls import path
from .views import AvailableBikesView, RentBikeView, ReturnBikeView, RentalHistoryView

urlpatterns = [
    path('available-bikes/', AvailableBikesView.as_view(), name='available_bikes'),
    path('rent-bike/', RentBikeView.as_view(), name='rent_bike'),
    path('return-bike/', ReturnBikeView.as_view(), name='return_bike'),
    path('rental-history/', RentalHistoryView.as_view(), name='rental_history'),
]
