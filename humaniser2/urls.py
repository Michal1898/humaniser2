"""humaniser2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from person_creator.models import Person
from person_creator.views import PeopleView, PeopleListView
admin.site.register(Person)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PeopleView.as_view(), name = 'index'),
    path('list/', PeopleListView.as_view(), name='people_list2')
]
