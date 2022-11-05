from django.urls import path
from .views import Arithmetic
app_name = "arithmetic"
urlpatterns = [
    path("api/", Arithmetic.as_view(), name="arithmetic"),
]