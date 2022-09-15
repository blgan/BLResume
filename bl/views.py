from django.shortcuts import render
from .models import About, Experience, Education, Skill, Language, Award


# Create your views here.


def mmdv(request):
    abts = About.objects.all()
    exps = Experience.objects.all()
    educ = Education.objects.all()
    skil = Skill.objects.all()
    lang = Language.objects.all()
    awd = Award.objects.all()
    return render(request, "index.html", {"abts": abts, "exps": exps, "educ": educ, "skil": skil, "lang": lang, "awd": awd})

# def index(request):
#   abts = About.objects.all()

#  return render(request, "index.html", {'abts': abts})


# def index(request):
#   exps = Experience.objects.all()

#  return render(request, "index.html", {'exps': exps})
