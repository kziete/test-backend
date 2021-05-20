class StartJourney:
    def __init__(self, repository, notifier):
        self.repository = repository
        self.notifier = notifier

    def execute(self):
        vehicle = self.repository.get_vehicle()
        if vehicle.max_capacity > 10:
            return True
