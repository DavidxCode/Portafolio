from django.shortcuts import render

from about.models import About

# Create your views here.
def index(request):
    About_me=About.objects.all()
    return render(request, 'core/index.html',{'About': About_me})
