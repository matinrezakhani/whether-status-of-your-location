import requests
import sys

def check_internet():
    url='http://www.google.com'
    timeout=5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False


def get_lon_lat():

    city = sys.argv[1]
    address = "http://api.openweathermap.org/data/2.5/weather?q="+city+",IR&appid=2dd6bf773ee43f327425048c5f8cf6f9"
    r = requests.get(url = address)
    return r.json()

def get_weather(lon,lat):
    address = "https://api.darksky.net/forecast/3e699a55f391aa1362d5a19b6b8a6445/"+str(lat)+","+str(lon)+"?units=si"
    r = requests.get(url = address)
    return r.json()

if(check_internet()==True):
    ll = get_lon_lat()
    lon = ll.get("coord").get("lon")
    lat = ll.get("coord").get("lat")

    data = get_weather(lon,lat)
    status = data.get("currently").get("summary")
    temp = data.get("currently").get("temperature")
    realfeel = data.get("currently").get("apparentTemperature")

    temp = round(temp)
    realfeel = round(realfeel)

    p = str(sys.argv[1])+" | "+str(status)+" | Temperature : "+str(temp)+" °C"
    #p = '|'+str(temp)+" °C"
    print(p)

else:
    print("|No Internet")
