from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from league.serializers import SeasonSerializer, SeasonDeserializer, UserSerializer
from league.models import Season
from league.epl import Table
from league.permissions import IsOwnerReadOnly


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SeasonList(generics.ListCreateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonDeserializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SeasonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly]

    def put(self, request, pk):
        data = request.data
        data._mutable = True
        season = data["season"]
        season_table = Table().select_season(season)
        data["winner"] = list(season_table["Team"])[0]
        data["second"] = list(season_table["Team"])[1]
        data["third"] = list(season_table["Team"])[2]
        data["fourth"] = list(season_table["Team"])[3]
        data["first_relegated"] = list(season_table["Team"])[17]
        data["second_relegated"] = list(season_table["Team"])[18]
        data["third_relegated"] = list(season_table["Team"])[19]

        return self.update(request, pk)
