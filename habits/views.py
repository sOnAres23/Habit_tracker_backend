from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.paginators import MyCustomPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwnerOrReadOnly


class IndexView(TemplateView):
    """Класс представления начальной страницы"""
    template_name = "habits/home.html"


class HabitViewSet(ModelViewSet):
    """Контроллер для представления привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = MyCustomPagination

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)

    def get_permissions(self):
        if self.action in ["update", "destroy"]:
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()

    def perform_update(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()

    def perform_destroy(self, serializer):
        new_habit = serializer.save()
        new_habit.delete()


class PublicHabitListApiView(generics.ListAPIView):
    """Контроллер на вывод только публичных привычек"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)
