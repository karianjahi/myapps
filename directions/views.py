from rest_framework import generics
from directions.serializers import DirectionSerializer
from directions.models import Direction
from directions.google_directions import Distance


class DirectionList(generics.ListCreateAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class DirectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

    def put(self, request, pk):
        data = request.data
        data._mutable = True
        print(data)
        destination = data["destination"]
        origin = data["origin"]
        distance_dict = Distance(origin, destination).get_attrs()
        data["distance"] = distance_dict["distance"]
        data["duration"] = distance_dict["duration"]
        return self.update(request, pk)
