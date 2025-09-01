from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Rubrique
from .serializer import RubriqueSerializer

class RubriqueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rubrique.objects.all()
    serializer_class = RubriqueSerializer
    #permission_classes = [IsAuthenticated]  permet d'authentifier l'utilisateur avant d'accéder aux données 
   #Filtrage et recherche
    filrerset_fields = ['title']
    search_fields = ['title', 'content']