from testapp import views
from django.urls import path
urlpatterns=[
    path("",views.users,name='users')
]