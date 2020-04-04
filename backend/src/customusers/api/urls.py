from django.urls import path
from .views import UserRUDView, UserAPIView

app_name = 'customusers'
urlpatterns = [
    path('', UserAPIView.as_view(), name='create'),
    path('<int:pk>/', UserRUDView.as_view(), name='student-rud'),



]