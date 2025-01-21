from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import validate_reward_and_related_habit, validate_duration, validate_related_habit_pleasant, \
    validate_pleasant_habit, validate_periodicity


class HabitSerializer(ModelSerializer):
    """Сериализатор для модели привычки"""
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [validate_reward_and_related_habit,
                      validate_duration,
                      validate_related_habit_pleasant,
                      validate_pleasant_habit,
                      validate_periodicity]
