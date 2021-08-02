from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from .serializers import UserSerializer, GroupSerializer, LinksSerializer
from .models import Link

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from links.tools import id_to_link, link_to_id


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class LinksViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinksSerializer
    permission_classes = [permissions.BasePermission]

    def list(self, request):
        queryset = Link.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def redirect(request, lk: str):
    if len(lk) > 5:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    l = get_object_or_404(Link.objects, link_id=link_to_id(lk))
    resp = Response(status=status.HTTP_301_MOVED_PERMANENTLY)
    resp['Location'] = l.url
    return resp
