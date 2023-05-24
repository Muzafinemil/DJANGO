from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'teams'

    def __str__(self):
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=50)
    age = models.IntegerField()
    country = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'игрок'
        verbose_name_plural = 'игроки'

    def __str__(self):
        return self.nickname


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    teams = models.ManyToManyField(Team)

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'

    def __str__(self):
        return self.name


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1_matches')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2_matches')
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    result = models.CharField(max_length=50)

    def get_date(self):
        start_date = self.start_datetime.date()
        end_date = self.end_datetime.date()
        return start_date, end_date

    class Meta:
        verbose_name = 'матч'
        verbose_name_plural = 'матчи'

    def __str__(self):
        return f'{self.team1} versus {self.team2}'
