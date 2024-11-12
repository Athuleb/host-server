from django.urls import path
from .views import FindDistance
urlpatterns = [
    path('',FindDistance.as_view(),name="FindDistance")
]