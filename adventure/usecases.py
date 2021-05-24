class StartJourney:
    def __init__(self, repository, notifier):
        self.repository = repository
        self.notifier = notifier

    def set_params(self, data):
        self.data = data
        return self

    def execute(self):
        vehicle = self.repository.create_vehicle(**self.data)
        if vehicle.can_start():
            self.notifier.send_notifications()
            return vehicle

        return None
