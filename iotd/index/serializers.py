from django.contrib.auth.models import User, Group
from index.models import *
from rest_framework import serializers


'''
write your model's serializer
ex)
class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = People
        fields = (
            'id', 'created_at', 'updated_at', 'name', 'num', 'email', 'tel', 'polynm', 'orignm', 'bthday',
            'hoovalsix', 'hoovalseven', 'emaill', 'secretary', 'secretary2', 'electionnum', 'reelegbnnm',
            'homep', 'staff', 'shrtnm', 'memtitle', 'hbbycd', 'star', 'freepartycount'
        )
'''
