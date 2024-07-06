from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Bike, Rental
from .serializers import BikeSerializer, RentalSerializer
from django.utils import timezone


class AvailableBikesView(APIView):
    """ Класс получения списка велосипедов """



    def get(self, request):
        bikes = Bike.objects.filter(is_available=True)
        serializer = BikeSerializer(bikes, many=True)
        return Response(serializer.data)

class RentBikeView(APIView):
    """ Класс аренды велосипеда """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        bike_id = request.data.get('bike_id')

        try:
            bike = Bike.objects.get(pk=bike_id, is_available=True)
        except Bike.DoesNotExist:
            return Response({'error': 'Велосипед не найден или уже занят'}, status=status.HTTP_400_BAD_REQUEST)

        # Проверка, что пользователь не арендует уже велосипед
        if Rental.objects.filter(user=user, end_time__isnull=True).exists():
            return Response({'error': 'Вы уже арендовали велосипед'}, status=status.HTTP_400_BAD_REQUEST)

        rental = Rental.objects.create(user=user, bike=bike)
        bike.is_available = False
        bike.save()

        serializer = RentalSerializer(rental)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ReturnBikeView(APIView):
    """ Класс возврата велосипеда """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        rental_id = request.data.get('rental_id')

        try:
            rental = Rental.objects.get(pk=rental_id, user=user, end_time__isnull=True)
        except Rental.DoesNotExist:
            return Response({'error': 'Аренда не найдена'}, status=status.HTTP_400_BAD_REQUEST)

        rental.end_time = timezone.now()
        rental.cost = calculate_cost(rental.start_time, rental.end_time)  # Функция расчета стоимости
        rental.save()

        bike = rental.bike
        bike.is_available = True
        bike.save()

        serializer = RentalSerializer(rental)
        return Response(serializer.data, status=status.HTTP_200_OK)

def calculate_cost(start_time, end_time):
    total_cost = (end_time - start_time) * Rental.cost
    return total_cost

class RentalHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        rentals = Rental.objects.filter(user=user).order_by('-start_time')
        serializer = RentalSerializer(rentals, many=True)
        return Response(serializer.data)
