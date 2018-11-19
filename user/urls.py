from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/<path:next>', views.login_view, name='login')
]
