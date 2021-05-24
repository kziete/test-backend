class StartJourney:
    def __init__(self, repository, notifier):
        self.repository = repository
        self.notifier = notifier

    def set_params(self, name, passengers):
        self.name = name
        self.passengers = passengers
        return self

    def execute(self):
        vehicle = self.repository.create_vehicle(self.name, self.passengers)
        if vehicle.can_start():
            self.notifier.send_notifications()
            return vehicle

        return None
