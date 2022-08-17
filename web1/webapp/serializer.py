from rest_framework import serializers
from webapp.models import Contact, Snacks

class SnacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snacks
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'id']