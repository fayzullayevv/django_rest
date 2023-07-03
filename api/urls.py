from django.urls import path
from .views import * 

urlpatterns = [
    path('bot-users/',BotUsersApiView.as_view()),
    path('feedbacks/',FeedbacksApiView.as_view()),
]