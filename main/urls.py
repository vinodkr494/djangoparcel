from django.urls import path
from main.views import *

app_name = "main"

urlpatterns = [
    path("", home, name="home"),
    path("customer/", customer_page, name="customer_page"),
    path("courier/", courier_page, name="courier_page"),
    path("sign-up/", sign_up, name="sign_up"),
]
