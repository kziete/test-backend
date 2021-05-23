import pytest

from adventure import models
from adventure import usecases
from adventure import repositories
from adventure import notifiers



class TestBasic:
    def test_basic(self):
        assert True


class TestVehicle:
    def test_can_start(self):
        vehicle = models.Vehicle()
        assert vehicle.can_start()


class MockJourneyRepository(repositories.JourneyRepository):
    def create_vehicle(self, name):
        return models.Vehicle(
            max_capacity=10,
            name=name
        )


class MockNotifier(notifiers.Notifier):
    def send_notifications(self):
        pass


class TestStartJourney:
    def test_start(self):
        repo = MockJourneyRepository()
        notifier = MockNotifier()
        usecase = usecases.StartJourney(repo, notifier)\
            .set_params("Kitt")
        vehicle = usecase.execute()

        assert vehicle.name == "Kitt"

