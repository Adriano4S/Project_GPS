from django.shortcuts import render

# Create your views here.

def index(request):
    template_html = 'index.html'
    return render(request, template_html)


def gps(request):
    template_html = 'gps.html'
    return render(request, template_html)


def abordagem(request):
    template_html = 'abordagem.html'
    return render(request, template_html)


def di(request):
    template_html = 'di.html'
    return render(request, template_html)


def speech(request):
    template_html = 'speech.html'
    return render(request, template_html)


def fechamento(request):
    template_html = 'fechamento.html'
    return render(request, template_html)


def live(request):
    template_html = 'live.html'
    return render(request, template_html)


def referidos(request):
    template_html = 'referidos.html'
    return render(request, template_html)




