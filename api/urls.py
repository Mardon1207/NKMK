from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('telefon', views.telefon, name='telefon'),
    path('telefonadmin', views.telefonadmin, name='telefonadmin'),
    # path('yangiliklar', views.yangiliklar, name='yangiliklar'),
    # path('yangiliklaradmin', views.yangiliklaradmin, name='yangiliklaradmin'),
    path('404', views.eroror, name='404'),
]
