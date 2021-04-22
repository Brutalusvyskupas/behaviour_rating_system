from django.urls import path

from .views import list_of_offices


app_name = 'offices'

urlpatterns = [
    path('', list_of_offices, name="list_of_offices"),
]
