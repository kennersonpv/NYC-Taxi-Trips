import folium

class Mark:
    def __init__(self,map):
        self.map = map

    def insertMarkPickup(self, pickup_latitude_collection, pickup_longitude_collection):
        if(len(pickup_latitude_collection) != len(pickup_longitude_collection)):
            return self.map

        i = 0
        while(i<len(pickup_latitude_collection)):
            try:
                folium.Marker(location=[pickup_latitude_collection[i],pickup_longitude_collection[i]]).add_to(self.map)
            except ValueError:
                continue

            i += 1
        
        return self.map


    def insertMarkDropoff(self, dropoff_latitude_collection, dropoff_longitude_collection):
        if(len(dropoff_latitude_collection) != len(dropoff_longitude_collection)):
            return self.map

        i = 0
        while(i<len(dropoff_latitude_collection)):
            try:
                folium.CircleMarker(location=[dropoff_latitude_collection[i],dropoff_longitude_collection[i]], radius=5).add_to(self.map)
            except ValueError:
                continue
            
            i += 1

        return self.map
    