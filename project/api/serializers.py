from django.contrib.auth.models import User, Group
from rest_framework import serializers
from project.api.models import Squad, Soldier


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class SquadSerializer(serializers.HyperlinkedModelSerializer):
    soldiers = serializers.HyperlinkedRelatedField(
        many=True,
        queryset=Soldier.objects.all(),
        view_name='soldier-detail'
    )

    class Meta:
        model = Squad
        fields = ('url', 'name', 'soldiers')


class SoldierSerializer(serializers.HyperlinkedModelSerializer):
    squad = serializers.HyperlinkedRelatedField(
        queryset=Squad.objects.all(),
        view_name='squad-detail'
    )

    class Meta:
        model = Soldier
        fields = ('url', 'name', 'role', 'squad')
