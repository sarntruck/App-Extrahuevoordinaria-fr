from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.counters_list.html),
]
