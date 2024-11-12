from django.urls import path
from .views import sendFeedbackClass


urlpatterns = [
    path('',sendFeedbackClass.as_view(),name='sendfeedback')
]