
import folium
from folium.map import Popup
import webbrowser
import json
from pprint import pprint

class Point(object):
    lat = 0
    long = 0
    src = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self, lat, long, src):
        self.lat = lat
        self.long = long
        self.src = src

def openJSON():

    with open('test.json') as f:
        data = json.load(f)
        pointList = []
        for point in data:
            source = point["_source"]["layers"]["eth"]["eth.src"]
            lat = float (point["_source"]["layers"]["j2735"]["j2735.MessageFrame_element"]["j2735.value_element"]["j2735.coreData_element"]["j2735.lat"])/10000000
            long = float (point["_source"]["layers"]["j2735"]["j2735.MessageFrame_element"]["j2735.value_element"]["j2735.coreData_element"]["j2735.long"])/10000000
            pointList.append(Point(lat,long,source))
        mapData(pointList)




def mapData(pointList):

    m = folium.Map(location=[pointList[0].lat,pointList[0].long], zoom_start=20)

    feature_group = folium.FeatureGroup("Locations")
    for i in range(len(pointList)):
        print str(pointList[i].lat)+","+str(pointList[i].long)
        feature_group.add_child(folium.CircleMarker(location=(pointList[i].lat,pointList[i].long), popup=Popup("Soruce: " + pointList[i].src, show=True), color = 'red'))
        m.add_child(feature_group)



    #m = folium.Map(location=())
    #folium.CircleMarker(location=(lat,long), popup=Popup("Soruce: " + src, show=True), color = 'red').add_to(m)
    m.save('map.html')



def openMap():

    url = "map.html"
    b = webbrowser.get().open(url,new=2)

def main():
    openJSON()
    openMap()

if __name__== "__main__":
  main()
