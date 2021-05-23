from django.urls import path

from adventure import views

urlpatterns = [
    path('start', views.StartJourneyAPIView.as_view())
]
