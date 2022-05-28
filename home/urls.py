from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("bmi/",views.bmi,name='bmi'),
    path("abc/",views.singup,name='abc'),
    path("login/",views.log_in,name='login'),
    path("profile/",views.profile,name='profile'),
    path("save/",views.sv,name='save'),
    path("logout/",views.log_out,name='logout'),
    path("delete/<int:id>",views.delete,name='delete'),

]