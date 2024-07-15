from django.urls import path, include
from .views import home, index, MyDetailView, register, Formsss, my_view, mediafiles
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'),name= 'login' ),
    path('<int:pk>/', MyDetailView.as_view(), name='mydetail'),
    path('', home, name = 'prof'),
    path('index/', index),
    path('register/', register, name = 'register'),
    path('Formsss/', Formsss ),
    path('my_view/', my_view),
    path('mediafiles/', mediafiles),
]
