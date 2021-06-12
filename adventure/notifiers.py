from django.core import mail

from adventure.models import Journey


class Notifier:
    def send_notifications(self, journey: Journey) -> None:
        mail.send_mail(
            "Subject here",
            #  f"Journey start: {journey.start.isoformat}",
            f"Journey start: {journey.start}",
            "from@example.com",
            ["sdiaz@talana.com"],
            fail_silently=False,
        )
