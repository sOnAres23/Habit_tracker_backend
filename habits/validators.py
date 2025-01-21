from django.core.exceptions import ValidationError


def validate_reward_and_related_habit(habit):
    """Валидатор на исключение одновременного выбора связанной привычки и вознаграждения"""
    if habit.get('reward') and habit.get('related_habit'):
        raise ValidationError("Заполнить можно только одно из двух полей: 'Награда' или 'Связанная привычка'.")


def validate_duration(habit):
    """Валидатор проверки, что время выполнения должно быть не больше 120 секунд"""
    if habit.get('time_to_complete') is None:
        raise ValidationError("Продолжительность выполнения привычки не может быть пустой.")
    if habit.get('time_to_complete') > 120:
        raise ValidationError("Продолжительность выполнения привычки не может превышать 120 секунд.")


def validate_related_habit_pleasant(habit):
    """Валидатор проверки, что в связанные привычки могут попадать только привычки с признаком приятной"""
    if habit.get('related_habit') and not habit.get('related_habit').sign_pleasant_habit:
        raise ValidationError("Связанные привычки должны быть с признаком 'Приятная привычка'.")


def validate_pleasant_habit(habit):
    """Валидатор проверки, что у приятной привычки не может быть вознаграждения или связанной привычки"""
    if habit.get('sign_pleasant_habit') and (habit.get('reward') or habit.get('related_habit')):
        raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")


def validate_periodicity(habit):
    """Валидатор на выполнение привычки не реже, чем 1 раз в 7 дней"""
    if habit.get('frequency') < 1 or habit.get('frequency') > 7:
        raise ValidationError("Периодичность должна быть от 1 до 7 дней.")
