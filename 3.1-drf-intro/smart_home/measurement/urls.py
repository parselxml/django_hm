from django.urls import path
from .views import SensorListCreateView, SensorRetrieveUpdateView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view(), name='sensors-list-create'),
    path('sensors/<pk>/', SensorRetrieveUpdateView.as_view(), name='sensors-retrieve-update'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurements-create'),
]