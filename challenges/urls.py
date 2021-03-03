from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("<int:month>",views.int_month_rederict),
    path("<str:month>",views.month_challenges,name = "month-challenges")
]
