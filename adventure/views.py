from rest_framework import generics

from adventure import serializers
from adventure import usecases
from adventure import repositories
from adventure import notifiers


class StartJourneyAPIView(generics.CreateAPIView):
    serializer_class = serializers.JourneySerializer

    def perform_create(self, serializer):
        repo = repositories.JourneyRepository()
        notifier = notifiers.Notifier()
        usecase = usecases.StartJourney(repo, notifier)\
            .set_params(serializer.validated_data["name"])
        usecase.execute()

