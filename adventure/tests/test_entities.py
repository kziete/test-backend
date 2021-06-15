from datetime import date

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


@pytest.mark.skip
class TestJourney:
    def test_is_finished(self):
        journey = models.Journey(start=date.today(), end=date.today())
        assert journey.is_finished()

    def test_is_not_finished(self):
        journey = models.Journey(start=date.today())
        assert not journey.is_finished()
