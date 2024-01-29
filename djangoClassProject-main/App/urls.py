from .views import Affiche_ListView

from . import views
from django.urls import path

urlpatterns=[
    path('index/',views.index),
    path('index_c/<int:classe>/',views.index_id),
    path ('Affiche/',views.template),
    path('bd/',views.Affiches),
    path ('Affiche_ListView/',Affiche_ListView.as_view(),name="LV")
    ,path('ajout/',views.add_project)
]