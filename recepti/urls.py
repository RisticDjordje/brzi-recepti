from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # pocetna stranica
    path('', views.IndexView.as_view(), name='index'),

    # stranica koja ce prikazivati recepte koje je moguce napraviti
    path('recepti/', views.ReceptiView.as_view(), name='recepti'),

    # stranica recepta
    path('recepti/<int:pk>/', views.DetailView.as_view(), name='detalji'),

    # stranica za registraciju
    path('registracija/', views.UserFormView.as_view(), name='registracija'),

    # prijavljivanje i odjavljivanje
    path('login/', auth_views.LoginView.as_view, {'template_name': 'recepti/login.html'}, name='prijavljivanje'),
    path('logout/', auth_views.LogoutView.as_view, {'next_page': '/'}, name='odjavljivanje'),

    # dodaj recept
    path('dodajrecept/', views.DodajView.as_view(), name='dodajrecept'),

    # zdrava ishrana
    path('zdravaishrana/', views.ZdravaIshranaView.as_view(), name='zdravaishrana'),
    # pdf
    # path('pdf/', views.GeneratePdf.as_view()),
]
