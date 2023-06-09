import geocoder #import geocoder module
import requests #import request to spott API from RapidAPI


def get_location():
    g = geocoder.ip('me') #get the location from the IP address
    url = "https://spott.p.rapidapi.com/places/ip/me"
    
    with open("assistant_functions\spottAPI.txt", "r") as token: #open the API token
        headers = {
	        "X-RapidAPI-Key": token.read(),
	        "X-RapidAPI-Host": "spott.p.rapidapi.com"
        }   

    response = requests.get(url, headers=headers)

    details = response.json() #get the response in json format

    location = details["country"]["name"] #get the location from the API
    state = store_Location(g)
    
    return f"You are currently located in {state} {location}" #return the location

def store_Location(g):
    state = g.state
    
    return state