from __future__ import annotations

from .notifiers import Notifier
from .repositories import JourneyRepository


class StartJourney:
    def __init__(
        self, repository: JourneyRepository, notifier: Notifier
    ) -> StartJourney:
        self.repository = repository
        self.notifier = notifier

    def set_params(self, data: dict) -> StartJourney:
        self.data = data
        return self

    def execute(self) -> None:
        vehicle = self.repository.create_vehicle(**self.data)
        if vehicle.can_start():
            self.notifier.send_notifications()
            return vehicle

        return None
