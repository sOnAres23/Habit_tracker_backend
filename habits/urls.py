from django.urls import path
from rest_framework.routers import DefaultRouter

from habits import views

app_name = 'habits'

router = DefaultRouter()
router.register(r"habits", views.HabitViewSet, basename="habits")

urlpatterns = [
    path("public_habits/", views.PublicHabitListApiView.as_view(), name="public_habits"),

] + router.urls
