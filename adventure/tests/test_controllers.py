from django.core import mail

from adventure import models, notifiers, repositories, usecases, views

from .test_usecases import MockJourneyRepository


class TestRepository:
    def test_create_vehicle(self, mocker):
        # se parcha para no probar métodos de la ORM
        mocker.patch.object(models.Vehicle.objects, "create")
        repo = repositories.JourneyRepository()
        repo.create_vehicle(name="a", passengers=10)
        assert models.Vehicle.objects.create.called


class TestNotifier:
    def test_send_notification(self, mocker):
        # se parcha para no probar métodos del framework
        mocker.patch.object(mail, "send_mail")
        notifier = notifiers.Notifier()
        notifier.send_notifications()
        assert mail.send_mail.called


class TestStartJourneyAPIView:
    def test_api(self, client, mocker):
        mocker.patch.object(
            views.StartJourneyAPIView,
            "get_repository",
            return_value=MockJourneyRepository(),
        )

        payload = {"name": "Kitt", "passengers": 2}
        response = client.post("/adventure/start/", payload)

        assert response.status_code == 201


# TODO: Insertar caso complejo

# TODO: Insertar caso con celery
