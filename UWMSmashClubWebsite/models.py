import uuid
from xml.dom.pulldom import CHARACTERS

from django.db import models
from django.db.models import UUIDField

BEST_OF_CHOICES = [("3", 3), ("5", 5)]
CHARACTERS = [  ("Mario", "mario"),
                ("Donkey Kong", "donkey kong"),
                ("Link", "link"),
                ("Samus", "samus"),
                ("Dark Samus", "dark samus"),
                ("Yoshi", "yoshi"),
                ("Kirby", "kirby"),
                ("Fox", "fox"),
                ("Pikachu", "pikachu"),
                ("Luigi", "luigi"),
                ("Ness", "ness"),
                ("Captain Falcon", "captain falcon"),
                ("Jigglypuff", "jigglypuff"),
                ("Peach", "peach"),
                ("Daisy", "daisy"),
                ("Bowser", "bowser"),
                ("Ice Climbers", "ice climbers"),
                ("Sheik", "sheik"),
                ("Zelda", "zelda"),
                ("Dr. Mario", "dr. mario"),
                ("Pichu", "pichu"),
                ("Falco", "falco"),
                ("Marth", "marth"),
                ("Lucina", "lucina"),
                ("Young Link", "young link"),
                ("Ganondorf", "ganondorf"),
                ("Mewtwo", "mewtwo"),
                ("Roy", "roy"),
                ("Chrom", "chrom"),
                ("Mr. Game & Watch", "mr. game & watch"),
                ("Meta Knight", "meta knight"),
                ("Pit", "pit"),
                ("Dark Pit", "dark pit"),
                ("Zero Suit Samus", "zero suit samus"),
                ("Wario", "wario"),
                ("Snake", "snake"),
                ("Ike", "ike"),
                ("Pokemon Trainer", "pokemon trainer"),
                ("Diddy Kong", "diddy kong"),
                ("Lucas", "lucas"),
                ("Sonic", "sonic"),
                ("King Dedede", "king dedede"),
                ("Olimar", "olimar"),
                ("Lucario", "lucario"),
                ("R.O.B.", "r.o.b."),
                ("Toon Link", "toon link"),
                ("Wolf", "wolf"),
                ("Villager", "villager"),
                ("Mega Man", "mega man"),
                ("Rosalina & Luma", "rosalina & luma"),
                ("Wii Fit Trainer", "wii fit trainer"),
                ("Little Mac", "little mac"),
                ("Greninja", "greninja"),
                ("Palutena", "palutena"),
                ("Pac-Man", "pac-man"),
                ("Robin", "robin"),
                ("Shulk", "shulk"),
                ("Bowser Jr.", "bowser jr."),
                ("Duck Hunt", "duck hunt"),
                ("Ryu", "ryu"),
                ("Ken", "ken"),
                ("Cloud", "cloud"),
                ("Corrin", "corrin"),
                ("Bayonetta", "bayonetta"),
                ("Inkling", "inkling"),
                ("Ridley", "ridley"),
                ("Simon", "simon"),
                ("Richter", "richter"),
                ("King K. Rool", "king k. rool"),
                ("Isabelle", "isabelle"),
                ("Incineroar", "incineroar"),
                ("Piranha Plant", "piranha plant"),
                ("Joker", "joker"),
                ("Hero", "hero"),
                ("Banjo & Kazooie", "banjo & kazooie"),
                ("Terry", "terry"),
                ("Byleth", "byleth"),
                ("Min Min", "min min"),
                ("Steve", "steve"),
                ("Sephiroth", "sephiroth"),
                ("Pyra/Mythra", "pyra/mythra"),
                ("Kazuya", "kazuya"),
                ("Sora", "sora"),
                ("Mii Brawler", "mii brawler"),
                ("Mii Swordfighter", "mii swordfighter"),
                ("Mii Gunner", "mii gunner")]

# Create your models here.
# Administrator Model
class Administrator(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.TextField(unique=True, blank=False, null=False)
    password = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.username

# Player Model
class Player(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.TextField(unique=True, blank=False, null=False)

    def __str__(self):
        return self.username


#Game Model
class Game(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    p1Char = models.CharField(max_length=32, blank=True, null=True, choices=CHARACTERS)
    p2Char = models.CharField(max_length=32, blank=True, null=True, choices=CHARACTERS)
    winner = models.ForeignKey(Player, related_name='game_winner', on_delete=models.SET_NULL, null=True, blank=True)
    loser = models.ForeignKey(Player, related_name='game_loser', on_delete=models.SET_NULL, null=True, blank=True)
    game_num = models.IntegerField(blank=False, null=False, default=1)

    def __str__(self):
        return winner.username + " vs. " + loser.username + "game #" + game_num


#Set Model
class Set(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    match_number = models.IntegerField(blank=False, null=False, default=1)
    player1 = models.ForeignKey(Player, related_name="player1", on_delete=models.SET_NULL, blank=True, null=True)
    player2 = models.ForeignKey(Player, related_name="player2", on_delete=models.SET_NULL, blank=True, null=True)
    winner = models.ForeignKey(Player, related_name='won_sets', on_delete=models.SET_NULL, null=True, blank=True)
    loser = models.ForeignKey(Player, related_name='lost_sets', on_delete=models.SET_NULL, null=True, blank=True)
    best_of_num = models.IntegerField(blank=False, null=False, choices=BEST_OF_CHOICES, default=3)
    games = models.ManyToManyField(Game)
    is_winners = models.BooleanField(blank=False, null=False, default=True)

    def __str__(self):
        return player1.username + " vs. " + player2.username


#Bracket Model
class Bracket(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(blank=False, null=False, default="Cream City Clash #XXX")
    matches = models.ManyToManyField(Set, related_name='bracket_sets')
    players = models.ManyToManyField(Player, related_name='brackets_entered')

    def __str__(self):
        return self.name

#SeedToPlacement Model
class SeedToPlacement(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    player = models.ForeignKey(Player, related_name='seed_and_placement', on_delete=models.SET_NULL, null=True, blank=True)
    seed = models.IntegerField(unique=True, blank=False, null=False, default=1)
    placement = models.IntegerField(blank=True, null=True)
    bracket = models.ForeignKey(Bracket, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return bracket.name + " Seeds and Results"