from django.urls import path
from dashboard import views

urlpatterns = [
    path('',views.display, name="dashboard"),
    path('newlead/',views.newlead, name="newlead"),
    path('hotlead/',views.hotlead, name="hotlead"),
    
   
]