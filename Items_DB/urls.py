from django.urls import path

from . import views

app_name = "itemsDB"
urlpatterns = [
    path("",views.index, name="index")
]