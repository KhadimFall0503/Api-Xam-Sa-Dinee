from rest_framework import serializers
from .models import Rubrique, Contenu

class ContenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenu
        fields = "__all__"   

class RubriqueSerializer(serializers.ModelSerializer):
    contenus = ContenuSerializer(many=True, read_only=True)
    
    class Meta:
        model = Rubrique
        fields = "__all__"
