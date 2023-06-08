import requests #import request to translation API from RapidAPI

def translate(text):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    
    src = fetchSource(text)

    payload = { 
               "q": text,
               "target": "es",
	           "source": src
    }
    
    with open("assistant_functions/translationAPI.txt", "r") as token:
        headers = {
	        "content-type": "application/x-www-form-urlencoded",
	        "Accept-Encoding": "application/gzip",
	        "X-RapidAPI-Key": token.read(),
	        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }

    response = requests.post(url, data=payload, headers=headers)

    return response.json()["data"]["translations"][0]["translatedText"] #return the translation

def fetchSource(text):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

    payload = { "q": text }
    headers = {
	    "content-type": "application/x-www-form-urlencoded",
	    "Accept-Encoding": "application/gzip",
	    "X-RapidAPI-Key": "423f18c5b4msh7244e14a76753c9p12f965jsn476fe09a8430",
	    "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)
    
    return response.json()["data"]["detections"][0][0]["language"]
    