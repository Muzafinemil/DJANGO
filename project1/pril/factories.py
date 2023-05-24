import factory
from  faker import  Factory
from .models import *

factory_ru = Factory.create('ru-Ru')


class TeamFactory(factory.django.DjangoModelFactory):
    name = factory_ru.word()
    country = factory_ru.word()
    rating = factory_ru.word()

    class Meta:
        model = Team
