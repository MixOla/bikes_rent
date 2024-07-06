from bikes.models import Bike

def test_bike_list(client):
    bike = Bike.objects.create(
        model = "Ворона",
        serial_number = 1,
        is_available = True
    )

    expected_response = {

    }