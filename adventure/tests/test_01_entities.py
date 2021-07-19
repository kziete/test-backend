from datetime import date

import pytest

from adventure import models

@pytest.fixture
def car():
    return models.VehicleType(max_capacity=5)


class TestVehicle:
    def test_capacity_greater_than_passengers(self, car):
        vehicle = models.Vehicle(
            vehicle_type=car, passengers=2
        )
        assert vehicle.can_start()

    def test_vehicle_overload(self, car):
        vehicle = models.Vehicle(
            vehicle_type=car, passengers=10
        )
        assert not vehicle.can_start()

    @pytest.mark.skip
    def test_vehicle_distribution(self, car):
        vehicle = models.Vehicle(
            vehicle_type=car, passengers=2
        )
        distribution_expected = [
            [True, True],
            [True, False],
        ]
        assert vehicle.get_distribution() == distribution_expected


@pytest.mark.skip
class TestJourney:
    def test_is_finished(self):
        journey = models.Journey(start=date.today(), end=date.today())
        assert journey.is_finished()

    def test_is_not_finished(self):
        journey = models.Journey(start=date.today())
        assert not journey.is_finished()
