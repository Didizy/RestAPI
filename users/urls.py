from django.urls import path, include
from .views import RegisterView, LoginView, UserView, ToDoShow, AddTask

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('todo/', AddTask.as_view()),
    path('todo/<int:pk>', AddTask.as_view()),
]