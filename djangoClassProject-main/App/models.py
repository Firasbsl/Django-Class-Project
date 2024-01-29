from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, MinValueValidator, MaxValueValidator
from django.db import models

def is_esprit_mail(mail):
    if (str(mail).endswith('@esprit.tn')):
        return True
    else:
        raise ValidationError("no valid email ",params={'mail': mail})

class User (models.Model):
     nom = models.CharField(max_length=150)
     prenom = models.CharField(max_length=150)
     email = models.EmailField('mail',validators=[is_esprit_mail])
     def __str__(self):
         return self.nom

class Etudiant (User):
        groupe = models.CharField(max_length=150)

class Coach(User):
    pass
class Project (models.Model):
        nom = models.CharField('titre du projet' ,max_length=150)
        duree_projet = models.IntegerField(default=0)
        temps_alloue_par_createur= models.IntegerField('Temps alloue',validators=[MinValueValidator(1),MaxValueValidator(10)])
        besoins = models.TextField(max_length=100)
        descriptions = models.TextField(max_length=100)
        est_valide=models.BooleanField(default=False)
        createur = models.OneToOneField(
            Etudiant,on_delete=models.CASCADE,
            related_name='project_owner'
        )
        superviseur = models.ForeignKey(
            Coach,
            on_delete=models.SET_NULL,
            null = True ,
            related_name='project_coach'
        )

        members = models.ManyToManyField(
            Etudiant,
            through='MemberShipInProject',
            related_name='Les_membres'
        )

class MemberShipInProject(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Etudiant,on_delete=models.CASCADE)
    Tim_allocated_by_memebers= models.IntegerField()