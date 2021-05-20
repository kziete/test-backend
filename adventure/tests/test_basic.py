import pytest

from adventure import models
from adventure import usecases
from adventure import repositories



class TestBasic:
    def test_basic(self):
        assert True


class TestVehicle:
    def test_can_start(self):
        vehicle = models.Vehicle()
        assert vehicle.can_start()


class MockJourneyRepository(repositories.JourneyRepository):
    def get_vehicle(self):
        return models.Vehicle(
            max_capacity=1
        )


class TestStartJourney:
    def test_start(self):
        repo = MockJourneyRepository()
        usecase = usecases.StartJourney(repo, None)
        usecase.execute()

