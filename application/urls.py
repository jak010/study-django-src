from django.urls import path
from application.views import PersonView

urlpatterns = [
    path("person", PersonView.as_view())
]
