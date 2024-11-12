from geopy.geocoders import Nominatim
from rest_framework.views import APIView
from django.http import JsonResponse
from geopy.distance import geodesic


class FindDistance(APIView):
    def get_coordinates(self,place):
        print('place',place)
        geolocator = Nominatim(user_agent="happy_journey")
        location = geolocator.geocode(place)
        print("location====",location)
    
        if location:
            return (location.latitude, location.longitude)
        else:
            return None
        
    

    def post(self,request):
        print("request>>>>>",request)
        try:
            data = request.data  
            print("data===>",data)
            start = data.get("from")

            destination = data.get("to")
            print("response>>",start,destination)

            
            coordinates1 = self.get_coordinates(start)
            coordinates2 = self.get_coordinates(destination)
            dist = geodesic(coordinates1,coordinates2).kilometers
            print(f"Distance from {start} to erappu is {dist:.2f} km")

            if coordinates1:
                print(f"Coordinates of {start}: {coordinates1}")
                return JsonResponse({
                    "start":start,
                    "ends":destination,
                    "coordinates1":coordinates1,
                    "coordinates2":coordinates2,
                    "distance":dist
                })

            else:
                print("Location not found.")
            
        except Exception as e:
            return JsonResponse({"error": f"Error fetching data: {e}"})
