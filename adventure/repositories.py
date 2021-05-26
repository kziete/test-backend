from adventure import models


class JourneyRepository:
    def create_vehicle(self, name: str, passengers: int) -> models.Vehicle:
        return models.Vehicle.objects.create(name=name, passengers=passengers)
