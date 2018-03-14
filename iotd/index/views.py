# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from index.models import *
from index.serializers import *
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PeopleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    
    '''
    if you want custom response,

    def TestPeople(self, request):
        people = People.objects.filter(category1="경제")
        serializer = PeopleSerializer(people, many=True)
        return Response(serializer.data)
    '''

