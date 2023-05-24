from .forms import *
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from . import filters

from .models import Tournament, Match, Team, Player


def index(request):
    return render(request=request, template_name='pril/index.html')


class TournamentPage(ListView):
    model = Tournament
    template_name = 'pril/turniri.html'
    context_object_name = 'tournaments'


class MatchPage(ListView):
    model = Match
    template_name = 'pril/matches.html'
    context_object_name = 'matchs'


class TeamPage(ListView):
    model = Team
    template_name = 'pril/teams.html'
    context_object_name = 'teams'

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filter()
        context['form'] = TeamSearch
        context['count'] = self.get_queryset().count()
        return context

    def get_filter(self):
        return filters.TeamFilter(self.request.GET)


class PlayersPage(ListView):
    model = Player
    template_name = 'pril/player.html'
    context_object_name = 'players'


class TitleMixin:
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_title()
        return context


class TeamADD(TitleMixin, CreateView):
    model = Team
    template_name = 'pril/teamsadd.html'
    success_url = reverse_lazy('team')
    title = 'Создание'
    form_class = TeamAdd


class TeamDelete(TitleMixin, DeleteView):
    model = Team
    template_name = 'pril/teamsdelete.html'
    success_url = reverse_lazy('team')
    title = 'Удаление'


class TeamUpdate(TitleMixin,UpdateView):
    model = Team
    template_name ='pril/teamsadd.html'
    success_url = reverse_lazy('team')
    title = 'Обновить'
    form_class = TeamAdd
