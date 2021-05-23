class StartJourney:
    def __init__(self, repository, notifier):
        self.repository = repository
        self.notifier = notifier

    def set_params(self, name):
        self.name = name
        return self

    def execute(self):
        vehicle = self.repository.create_vehicle(self.name)
        if vehicle.can_start() and vehicle.max_capacity >= 10:
            self.notifier.send_notifications()
            return vehicle
