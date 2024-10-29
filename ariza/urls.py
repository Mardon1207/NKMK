from django.urls import path

from .views import (
    ApplicationListView,
    ApplicationDetailView,
    ApplicationCreateView,
    QabulCreateView,
    QabulDetailView
)

urlpatterns = [
    path('<int:pk>/', ApplicationDetailView.as_view(), name='application_detail'),
    path('new/', ApplicationCreateView.as_view(), name='application_new'),
    path('', ApplicationListView.as_view(), name='application'),
    path('<int:pk>/qabul/', QabulCreateView.as_view(), name='qabul_new'),
    path('qabul/<int:pk>/', QabulDetailView.as_view(), name='qabul_detail'),

]