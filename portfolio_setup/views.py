from django.shortcuts import render, HttpResponse
# Create your views here.
# request --> response
# request handler


def home(request):
    return render(request, "home.html")


def chess(request):
    return render(request, "chess.html")


def dataScraper(request):
    return render(request, "dataScraper.html")


def imageScrambler(request):
    return render(request, "imageScrambler.html")


def resume(request):
    return render(request, "resume.html")
