from django.urls import path, include
from .views import SpamView

urlpatterns = [
    path('',SpamView, name='spam_view' )
]