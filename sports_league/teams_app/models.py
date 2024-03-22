from django.db import models

class Conference(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    conference = models.ForeignKey(Conference, related_name='teams', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.location} {self.name}"

class Player(models.Model):
    team = models.ForeignKey(Team, related_name='players', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    age = models.IntegerField()
    is_injured_reserve = models.BooleanField(default=False)
    points_per_game = models.IntegerField(default=0) 

    def __str__(self):
        return self.name

