from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="ShopHone"),
    path("contact/", views.contact, name="contact"),
    path("search/", views.search, name="search"),
    path("product/<int:myid>", views.productView),
    path('order/',views.checkout),
    path("tracker/", views.tracker, name="tracker"),
]
