from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import bookingSerializer, menuSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer


class BookingViewSet (viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message": "This view is protected"})
