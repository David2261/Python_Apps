from django.urls import path
from .views import HomePage


app_name = 'botrequest'
urlpatterns = [
    # path('', views.index, name="main-view" ),
    path('', HomePage.as_view(), name="home_page"),
]
