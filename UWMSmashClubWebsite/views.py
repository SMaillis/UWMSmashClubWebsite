from django.shortcuts import render
from django.views import View
from datetime import datetime

# Create your views here.
class HomePage(View):
    def get(self, request):
        #get the time and format it to appear properly using strftime
        now = datetime(2025, 9, 5, 16, 30, 0).isoformat()
        return render(request, 'home.html',{"now": now})

    def post(self, request):
        pass


class BracketArchivePage(View):
    def get(self, request):
        return render(request, 'bracket-archive.html')

    def post(self, request):
        pass


class PowerRankingsPage(View):
    def get(self, request):
        return render(request, 'power-rankings.html')

    def post(self, request):
        pass


class PlayerStatsPage(View):
    def get(self, request):
        return render(request, 'player-stats.html')

    def post(self, request):
        pass


class SeedingToolPage(View):
    def get(self, request):
        return render(request, 'seeding-tool.html')

    def post(self, request):
        pass


class AboutClubPage(View):
    def get(self, request):
        return render(request, 'about-club.html')

    def post(self, request):
        pass


class AboutMePage(View):
    def get(self, request):
        return render(request, 'about-me.html')

    def post(self, request):
        pass


class AboutWebsitePage(View):
    def get(self, request):
        return render(request, 'about-website.html')

    def post(self, request):
        pass


class LoginPage(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        pass
