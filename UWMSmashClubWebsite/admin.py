from django.contrib import admin

from UWMSmashClubWebsite.models import Administrator, Player, Set, Game, SeedToPlacement, Bracket

# Register your models here.
admin.site.register(Administrator)
admin.site.register(Player)
admin.site.register(Set)
admin.site.register(SeedToPlacement)
admin.site.register(Game)
admin.site.register(Bracket)

