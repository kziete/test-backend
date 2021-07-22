from django.utils import timezone

from adventure import models


class JourneyRepository:
    def create_vehicle(self, name: str, passengers: int) -> models.Vehicle:
        return models.Vehicle.objects.create(name=name, passengers=passengers)

    def create_journey(self, vehicle: models.Vehicle) -> models.Journey:
        return models.Journey.objects.create(
            vehicle=vehicle, start=timezone.now().date()
        )
