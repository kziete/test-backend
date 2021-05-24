from rest_framework import generics

from adventure import notifiers, repositories, serializers, usecases


class StartJourneyAPIView(generics.CreateAPIView):
    serializer_class = serializers.JourneySerializer

    def perform_create(self, serializer):
        repo = self.get_repository()
        notifier = notifiers.Notifier()
        usecase = usecases.StartJourney(repo, notifier).set_params(
            **serializer.validated_data
        )
        usecase.execute()

    def get_repository(self):
        return repositories.JourneyRepository()
