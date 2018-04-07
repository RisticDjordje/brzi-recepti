from django.urls import path
from . import views

urlpatterns = [
    # pocetna stranica
    path('', views.IndexView.as_view(), name='index'),

    # stranica koja ce prikazivati recepte koje je moguce napraviti
    path('recepti/', views.ReceptiView.as_view(), name='recepti'),

    # stranica recepta
    path('recepti/<int:pk>/', views.DetailView.as_view(), name='detalji'),

    # stranica za registraciju
    path('registracija/', views.UserFormView.as_view(), name='registracija'),

]
