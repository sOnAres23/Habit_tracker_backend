from datetime import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_message


@shared_task
def send_habit_for_user():
    """Задача для напоминания о привычке пользователю в телеграм"""

    current_time = datetime.now().time().replace(second=0).strftime('%H:%M:%S')
    habits = Habit.objects.filter(sign_pleasant_habit=False)

    for habit in habits:
        habit_time = habit.time.strftime('%H:%M:%S')
        if current_time == habit_time:
            message = (f"Напоминание: {habit.action}, в {habit.time.strftime('%H:%M')},"
                       f" место: {habit.place}❤ за это приятность: {habit.reward}😊")
            chat_id = habit.user.tg_chat_id
            send_message(chat_id=chat_id, message=message)
