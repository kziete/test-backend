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
    def send_notifications(self, journey: models.Journey):
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

    def test_cant_start(self):
        repo = MockJourneyRepository()
        notifier = MockNotifier()
        data = {"name": "Kitt", "passengers": 6}
        usecase = usecases.StartJourney(repo, notifier).set_params(data)
        with pytest.raises(usecases.StartJourney.CantStart):
            journey = usecase.execute()


class TestStopJourney:
    @pytest.mark.skip
    def test_stop(self):
        # TODO: Implement a StopJourney Usecase
        # that it take a started journey as a parameter and set a "end" value
        # then save it to the database
        pass
