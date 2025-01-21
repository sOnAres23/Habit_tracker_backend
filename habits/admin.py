from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "place", "time", "action", "sign_pleasant_habit", "related_habit",
                    "frequency", "reward", "time_to_complete", "is_public")
    list_filter = ("action",)
    search_fields = ("action", "place",)
