import pytest

from adventure import models, notifiers, repositories, usecases, views


class TestBasic:
    def test_basic(self):
        assert True


class TestVehicle:
    def test_can_start(self):
        vehicle = models.Vehicle(
            vehicle_type=models.VehicleType(max_capacity=5), passengers=2
        )
        assert vehicle.can_start()


class MockJourneyRepository(repositories.JourneyRepository):
    def create_vehicle(self, name, passengers):
        v_type = models.VehicleType(name="car", max_capacity=5)
        return models.Vehicle(name=name, passengers=passengers, vehicle_type=v_type)


class MockNotifier(notifiers.Notifier):
    def send_notifications(self):
        pass


class TestStartJourney:
    def test_start(self):
        repo = MockJourneyRepository()
        notifier = MockNotifier()
        data = {"name": "Kitt", "passengers": 2}
        usecase = usecases.StartJourney(repo, notifier).set_params(data)
        vehicle = usecase.execute()

        assert vehicle.name == "Kitt"


class TestStartJourneyAPIView:
    def test_api(self, client, mocker):
        mocker.patch.object(
            views.StartJourneyAPIView,
            "get_repository",
            return_value=MockJourneyRepository(),
        )

        payload = {"name": "Kitt", "passengers": 2}
        response = client.post("/adventure/start/", payload)

        assert response.status_code == 201
