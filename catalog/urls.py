from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("", views.home, name="home"),
    path("product/<int:product_id>/set_alert/", views.set_alert, name="set_alert"),
    path("save_product/", views.save_product, name="save_product"),
    path("product/<int:product_id>/delete/", views.delete_product, name="delete_product"), 
]

