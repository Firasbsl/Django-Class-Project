from .models import Project
from django import forms


class AddProjectForm(forms.ModelForm):
    class Meta :
        model=Project
        fields = ('nom','duree_projet','temps_alloue_par_createur','besoins','descriptions','est_valide','createur')
