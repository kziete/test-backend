import pytest
from django.utils import timezone

from adventure import models, notifiers, repositories, usecases

#########
# Mocks #
#########


class MockJourneyRepository(repositories.JourneyRepository):
    def create_vehicle(self, name, passengers):
        v_type = models.VehicleType(name="car", max_capacity=5)
        return models.Vehicle(name=name, passengers=passengers, vehicle_type=v_type)

    def create_journey(self, vehicle):
        return models.Journey(vehicle=vehicle, start=timezone.now().date())


class MockNotifier(notifiers.Notifier):
    def send_notifications(self):
        pass


#########
# Tests #
#########
class TestStartJourney:
    def test_start(self):
        repo = MockJourneyRepository()
        notifier = MockNotifier()
        data = {"name": "Kitt", "passengers": 2}
        usecase = usecases.StartJourney(repo, notifier).set_params(data)
        journey = usecase.execute()

        assert journey.vehicle.name == "Kitt"


class TestStopJourney:
    @pytest.mark.skip
    def test_stop(self):
        # TODO: Implement a StopJourney Usecase
        pass
