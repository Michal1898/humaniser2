from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from person_creator.humaniser.humaniser import random_person
from person_creator.models import Person

class PeopleView(View):
  def get(self, request):
    m=random_person()
    print(m)
    return render(
      request, template_name='person_list_1.html' ,
      context={'people' : Person.objects.all()}
    )

class PeopleListView(ListView):
  template_name = 'person_list_2.html'
  model = Person