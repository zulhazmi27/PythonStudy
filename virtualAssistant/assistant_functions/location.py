import geocoder #import geocoder module

def get_location():
    g = geocoder.ip('me') #get the location from the IP address
    
    return f"You are currently located in {g.city}, {g.state}" #return the location
