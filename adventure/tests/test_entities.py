import pytest

from adventure import models


class TestVehicle:
    def test_capacity_greater_than_passengers(self):
        vehicle = models.Vehicle(
            vehicle_type=models.VehicleType(max_capacity=5), passengers=2
        )
        assert vehicle.can_start()

    def test_vehicle_overload(self):
        vehicle = models.Vehicle(
            vehicle_type=models.VehicleType(max_capacity=5), passengers=10
        )
        assert not vehicle.can_start()


# TODO: Insertar caso complejo
