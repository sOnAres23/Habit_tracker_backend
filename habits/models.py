from django.db import models


class Habit(models.Model):
    """Модель создания привычки"""
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True, related_name="user",
                             verbose_name="Создатель привычки")
    place = models.CharField(max_length=255, verbose_name="Место привычки", help_text="Выберите место для привычки")
    time = models.TimeField(verbose_name="Время выполнения привычки", help_text="Укажите время для выполнения привычки")
    action = models.CharField(max_length=255, verbose_name="Действие привычки", help_text="Выберите действие привычки")
    sign_pleasant_habit = models.BooleanField(default=False, verbose_name="Приятная привычка",
                                              help_text="Признак на приятную привычку")
    related_habit = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True,
                                      verbose_name="Связанная привычка",
                                      help_text="Связанную привычку можно не указывать")
    frequency = models.PositiveIntegerField(default=1, verbose_name="Частота привычки",
                                            help_text="Укажите периодичность выполнения привычки в днях")
    reward = models.CharField(max_length=255, blank=True, null=True, verbose_name="Награда за выполнение привычки",
                              help_text="Награду можно не указывать")
    time_to_complete = models.PositiveIntegerField(verbose_name="Время выполнение в секундах(не больше 120 с)",
                                                   default=120, help_text="Укажите время выполнения привычки")
    is_public = models.BooleanField(default=True, verbose_name="Публичность привычки", help_text="Указать публичность")

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
