from django.urls import path
from ShowData import views
urlpatterns = [
    path('',views.index,name="home"),
    path('predict/',views.predict,name="predict"),
]
