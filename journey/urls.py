from django.urls import path
from .views import DestinationListView,FindWeather,SearchResult,GalleryView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/top-destinations/',DestinationListView.as_view({'get': 'list', 'post': 'create','put': 'update'}),name='destination-list'),
    path('api/top-destinations/<int:pk>/',DestinationListView.as_view({'get':'retrieve'}),name='destination-list'),
    path('api/weather/', FindWeather.as_view(), name='find_weather'),
    path('api/search/',SearchResult.as_view(),name="search-result"),
    path('api/gallery/', GalleryView.as_view(), name='gallery-view')
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)