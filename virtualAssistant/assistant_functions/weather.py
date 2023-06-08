import requests #import request to weather API from RapidAPI

def get_weather():
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":"Kuala Lumpur","lang":"en","units":"metric"}
    
    with open("assistant_functions\weatherApi.txt", "r") as token:
        headers = {
            "X-RapidAPI-Key": token.read(),
	        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

    response = requests.get(url, headers=headers, params=querystring) #get the response from the API
    
    details = response.json() #get the response in json format
    
    temperature = details["current"]["temp_c"]
    location = details["location"]["name"]
    country = details["location"]["country"]
    feelsliketemp = details["current"]["feelslike_c"]
    
    return f"The temperature is {temperature} degree celsius in {location} {country} right now, but it can feels like {feelsliketemp} degree celcius" #return the temperature and location
