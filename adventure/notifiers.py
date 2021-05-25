from django.core import mail


class Notifier:
    def send_notifications(self):
        mail.send_mail(
            "Subject here",
            "Here is the message.",
            "from@example.com",
            ["kziete@gmail.com"],
            fail_silently=False,
        )
