from django.contrib import admin
from django.urls import path,include
from profileapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profileapp.urls')),

]