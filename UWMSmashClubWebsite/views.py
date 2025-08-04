from django.shortcuts import render
from django.views import View

# Create your views here.
class HomePage(View):
    def get(self, request):
        return render(request, 'home.html')

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


class AboutPage(View):
    def get(self, request):
        return render(request, 'about.html')

    def post(self, request):
        pass


class LoginPage(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        pass
