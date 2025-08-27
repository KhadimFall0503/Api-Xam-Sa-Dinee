from rest_framework import viewsets
from .models import Rubrique
from .serializer import RubriqueSerializer

class RubriqueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rubrique.objects.all()
    serializer_class = RubriqueSerializer
