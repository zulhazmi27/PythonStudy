import requests #import request to weather API from RapidAPI

def get_weather():
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":"Kuala Lumpur","lang":"en","units":"metric"}

    headers = {
	    "X-RapidAPI-Key": "423f18c5b4msh7244e14a76753c9p12f965jsn476fe09a8430",
	    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    details = response.json() #get the response in json format
    
    temperature = details["current"]["temp_c"]
    location = details["location"]["name"]
    country = details["location"]["country"]
    feelsliketemp = details["current"]["feelslike_c"]
    
    return f"The temperature is {temperature} degree celsius in {location} {country} right now, but it can feels like {feelsliketemp} degree celcius" #return the temperature and location

