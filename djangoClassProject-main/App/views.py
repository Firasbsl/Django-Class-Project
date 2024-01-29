from App.models import Project
from .forms import AddProjectForm
from django.urls import reverse


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView


def index (request):
    return  HttpResponse ("Bonjour 4TWIN3")
def index_id(request,classe):
    return HttpResponse("Bonjour %s"%classe)

def template(request):
    return render(request,'App/Affiche.html')
def Affiches(request):
    projet = Project.objects.all()
    resultat = '-'.join([p.nom for p in projet])
   # return HttpResponse(resultat)
    return render(request,'App/Affiche.html',{'pp':projet})

class Affiche_ListView(ListView):
    model = Project
    template_name = "App/Affiche.html"
    context_object_name = 'pp'
def add_project (request):
    if request.method=='GET':
        form=AddProjectForm()
        return render(reqquest,'App/ajout.html',{'f':form})
    if request.method=='POST':
        form = AddProjectForm(request.POST)
        if form.is_valid():
            new_project=form.save(commit=False);
            new_project.save();
            return HttpResponseRedirect(reverse('LV'))
        else:
            return render(reqquest,'App/ajout.html',{'f':form,'msg_erreur':'Erreur lors de lajout'})
