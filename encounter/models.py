from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, TextInput, Textarea

class Encounter(models.Model):
    author = models.ForeignKey(User, verbose_name="author")
    name = models.CharField(max_length=40)
    campaign = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class EncounterForm(ModelForm):
    class Meta:
        model = Encounter
        exclude = ('author')
        widgets = {
            'campaign': TextInput(attrs={'class': 'input-block-level'}),
            'name': TextInput(attrs={'class': 'input-block-level'}),
            'description': Textarea(attrs={'class': 'input-block-level'}),
            }

class Entity(models.Model):
    encounter = models.ForeignKey(Encounter)
    name = models.CharField(max_length=40)
    initiative = models.IntegerField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

class EntityForm(ModelForm):
    class Meta:
        model = Entity
        fields = ('name',)
        widgets = {
            'name': TextInput(attrs={'class': 'input-block-level'}),
            }