from django.contrib import admin
from django.urls import path
from .views import EditorView

urlpatterns = [
    path("", EditorView.as_view()),
]