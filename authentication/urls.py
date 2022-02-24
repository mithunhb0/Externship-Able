from django.urls import path
from authentication import views

urlpatterns = [
    path('',views.register, name="register"),
    path('login/',views.login, name="login"),
    path('logout/',views.logout, name="logout"),
    path('test/',views.test, name="test"),
    
    
    
]