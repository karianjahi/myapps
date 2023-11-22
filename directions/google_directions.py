import googlemaps
GOOGLE_API_KEY = "AIzaSyArb_nNkFSFsEVJD-02IVVGL2VfpcTNmto"


class Distance:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.get_distance_matrix()

    def get_distance_matrix(self):
        client = googlemaps.Client(GOOGLE_API_KEY)
        self.distance_matrix = client.distance_matrix(self.origin, self.destination)

    def get_attrs(self):
        mongreal = self.distance_matrix["rows"][0]["elements"][0]
        distance = mongreal["distance"]["text"]
        duration = mongreal["duration"]["text"]
        return {"distance": distance,
                "duration": duration}


if __name__ == "__main__":
    obj = Distance("Berlin", "Leipzig")
    print(obj.get_attrs())
