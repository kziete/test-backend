import pytest

from adventure import models, notifiers, repositories, usecases, views


class TestBasic:
    def test_basic(self):
        assert True


class TestVehicle:
    def test_can_start(self):
        vehicle = models.Vehicle()
        assert vehicle.can_start()


class MockJourneyRepository(repositories.JourneyRepository):
    def create_vehicle(self, name):
        return models.Vehicle(max_capacity=10, name=name)


class MockNotifier(notifiers.Notifier):
    def send_notifications(self):
        pass


class TestStartJourney:
    def test_start(self):
        repo = MockJourneyRepository()
        notifier = MockNotifier()
        usecase = usecases.StartJourney(repo, notifier).set_params("Kitt")
        vehicle = usecase.execute()

        assert vehicle.name == "Kitt"


class TestStartJourneyAPIView:
    def test_api(self, client, mocker):
        mocker.patch.object(
            views.StartJourneyAPIView,
            "get_repository",
            return_value=MockJourneyRepository(),
        )

        payload = {"name": "Kitt"}
        response = client.post("/adventure/start/", payload)

        assert response.status_code == 201
