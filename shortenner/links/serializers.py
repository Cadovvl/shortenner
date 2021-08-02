import random

from django.contrib.auth.models import User, Group
from rest_framework import serializers

from links.models import Link
from links.tools import id_to_link, MAX_IDX


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class LinksSerializer(serializers.ModelSerializer):
    short_url = serializers.CharField(source='get_short_url', read_only=True)

    class Meta:
        model = Link
        fields = ['link_id', 'author', 'url', 'short_url']
        read_only_fields = ['link_id', 'short_url']

    def create(self, validated_data):
        l = Link(**validated_data)
        i = random.randint(0, MAX_IDX - 1)
        l.link_id = i
        l.save()
        return l


