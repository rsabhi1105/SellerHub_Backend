from django.urls import path

from contact.views import ContactView

urlpatterns = [
    path("contact/", ContactView.as_view()),
]
