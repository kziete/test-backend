from django.core import mail


class Notifier:
    def send_notifications(self) -> None:
        mail.send_mail(
            "Subject here",
            "Here is the message.",
            "from@example.com",
            ["sdiaz@talana.com"],
            fail_silently=False,
        )
