# from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from project.api.serializers import (
    UserSerializer, GroupSerializer, SquadSerializer, SoldierSerializer
    )
from project.api.models import Squad, Soldier


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SquadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer


class SoldierViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Soldier.objects.all()
    serializer_class = SoldierSerializer
