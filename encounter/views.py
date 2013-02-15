from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from encounter.models import *

def index(request):
    # use current user
    encounters = Encounter.objects.filter(
        author_id=1
        )
    newEncounterForm = EncounterForm()
    return render_to_response('encounter/index.html',
                              {'encounterList': encounters,
                               'newEncounterForm': newEncounterForm},
                              context_instance=RequestContext(request))

def add(request):
    # use current user
    encounter = Encounter(author = User.objects.get(pk=1))
    form = EncounterForm(request.POST, instance=encounter)
    if (form.is_valid()):
        form.save()
        return HttpResponse(str(encounter.id), status=200)
    else:
        return HttpResponse(status=400)

def delete(request, encounter_id):
    # should require auth check that current user is author
    Encounter.objects.get(pk=encounter_id).delete();
    return HttpResponse(status=200)

def edit(request, encounter_id):
    # should require auth check that current user is author
    encounter = Encounter.objects.get(pk=encounter_id)
    entities = Entity.objects.filter(encounter_id=encounter_id)
    newEntityForm = EntityForm()
    return render_to_response('encounter/edit.html',
        {'encounter': encounter,
         'entities': entities,
         'newEntityForm': newEntityForm},
        context_instance=RequestContext(request))

def add_entity(request, encounter_id):
    # use current user
    entity = Entity(encounter = Encounter.objects.get(pk=encounter_id))
    form = EntityForm(request.POST, instance=entity)
    if (form.is_valid()):
        form.save()
        return HttpResponse(str(entity.id), status=200)
    else:
        print form.errors
        return HttpResponse(status=400)