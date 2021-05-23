from adventure import models


class JourneyRepository:
    def create_vehicle(self, name):
        return models.Vehicle.objects.create(name=name)
