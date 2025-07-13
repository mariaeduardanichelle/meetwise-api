from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Event, Registration, User

class EventAppTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="testpass123")
        self.event = Event.objects.create(name="Evento 1", description="Desc", date="2025-12-30")

    def test_event_creation_requires_auth(self):
        url = reverse("event-list")
        data = {"name": "Novo Evento", "description": "Descrição", "date": "2025-12-31"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 401) 

    def test_event_creation_authenticated(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("event-list")
        data = {"name": "Novo Evento", "description": "Descrição", "date": "2025-12-31"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_for_event(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("registration-create")
        data = {"event_id": self.event.id}  
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_registrations_view(self):
        Registration.objects.create(user=self.user, event=self.event)
        self.client.force_authenticate(user=self.user)
        url = reverse("user-registrations", kwargs={"user_id": self.user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
