from adventure import models


class JourneyRepository:
    def get_vehicle(self):
        return models.Vehicle.objects.first()
