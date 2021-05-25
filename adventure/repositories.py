from adventure import models


class JourneyRepository:
    def create_vehicle(self, name, passengers):
        return models.Vehicle.objects.create(name=name, passengers=passengers)
