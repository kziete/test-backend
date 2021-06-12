from __future__ import annotations

from .notifiers import Notifier
from .repositories import JourneyRepository


class StartJourney:
    def __init__(self, repository: JourneyRepository, notifier: Notifier):
        self.repository = repository
        self.notifier = notifier

    def set_params(self, data: dict) -> StartJourney:
        # self._data = data
        self.data = data
        return self

    def execute(self) -> None:
        vehicle = self.repository.create_vehicle(**self.data)
        if not vehicle.can_start():
            raise StartJourney.Exception("vehicle can't start")

        journey = self.repository.create_journey(vehicle)
        self.notifier.send_notifications(journey)
        return journey

    class Exception(Exception):
        pass
