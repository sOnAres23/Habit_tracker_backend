from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTrackerTestCase(APITestCase):
    """Класс тестирования модели привычки"""
    def setUp(self):
        self.user = User.objects.create(
            email="test@example.com",
            password="password123",
            tg_chat_id="123456789"
        )

        self.habit = Habit.objects.create(
            user=self.user,
            place="Дом",
            time="12:30:00",
            action="Поприседать",
            sign_pleasant_habit=False,
            frequency=1,
            reward="сьесть конфетку",
            time_to_complete=60,
            is_public=True
        )

        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """Тестирование создания привычки"""
        url = reverse("habits:habits-list")
        data = {
            "user": 1,
            "place": "Дом",
            "time": "12:30:00",
            "action": "Поприседать",
            "sign_pleasant_habit": False,
            "frequency": 1,
            "reward": "сьесть конфетку",
            "time_to_complete": 60,
            "is_public": True
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["place"], data["place"])
        self.assertEqual(response.json()["action"], data["action"])
        self.assertEqual(response.json()["time_to_complete"], data["time_to_complete"])

    def test_retrieve_all_habit(self):
        """Тестирование на вывод списка всех привычек"""
        url = reverse("habits:habits-list")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_public_habits(self):
        """Тестирование на просмотр публичных привычек"""
        url = reverse("habits:public_habits")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_duration_validation(self):
        """Тест по валидации продолжительности привычки"""
        url = reverse("habits:habits-list")
        data = {
            "place": "Стадион",
            "time": "07:00:00",
            "action": "Заниматься спортом",
            "sign_pleasant_habit": False,
            "frequency": 1,
            "reward": None,
            "time_to_complete": 150,
            "is_public": False,
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            "Продолжительность выполнения привычки не может превышать 120 секунд.", str(response.data),)

    def test_habit_periodicity_validation(self):
        """Тест по валидации периодичности привычки"""
        url = reverse("habits:habits-list")
        data = {
            "place": "Стадион",
            "time": "07:00:00",
            "action": "Заниматься спортом",
            "sign_pleasant_habit": False,
            "frequency": 8,
            "reward": None,
            "time_to_complete": 150,
            "is_public": False,
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Периодичность должна быть от 1 до 7 дней.", str(response.data))
