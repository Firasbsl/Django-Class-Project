from django.contrib import messages

from .models import *
from django.contrib import admin




class members(admin.StackedInline):
      model = MemberShipInProject
      extra = 0

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    def setToValid(self,request,queryset):
        rows = queryset.filter(est_valide=True)
        a = rows.count()
        if a> 0 :
           messages.error(request,"%s  projets  valide "% a)
        else:
              updated= queryset.update(est_valide=True)
              if updated ==1 :
                 message = "1 project was updates"
              else:
                message="%s projects where updates" %updated
              self.message_user(request,message)

    setToValid.short_description="Valider"
    actions = ['setToValid']
    list_per_page = 2
    search_fields = ['nom','duree_projet']
    list_display = ('nom','duree_projet','temps_alloue_par_createur','descriptions','besoins','est_valide')
    inlines = (members,)
    actions_on_top = False
    actions_on_bottom = True
    list_filter = ('est_valide','createur')



@admin.register(Etudiant)
class ProjectEtd(admin.ModelAdmin):
    def tester(self,request,queryset):
        queryset.update(nom="aymen")
    tester.short_description="ChangeName"
    actions=['tester']
    search_fields = ['nom']
    list_display =('nom','prenom','email')
#admin.site.register(Etudiant)
#admin.site.register(Project,ProjectAdmin)
admin.site.register(Coach)
#admin.site.register(MemberShipInProject)

@admin.register(User)
class ProjectCoach(admin.ModelAdmin):
    def setName(self,request,queryset):
        queryset.update(nom="hello")
    setName.short_description="setter"
    actions = ["setName"]
    search_fields = ['nom']
    list_display = ('nom','prenom','email')



