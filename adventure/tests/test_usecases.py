from adventure import models, notifiers, repositories, usecases


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


# TODO: Insertar caso complejo
