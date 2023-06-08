from datetime import datetime #import the datetime module

def get_dateTime():
    now = datetime.now() #get the current date and time'
    time = now.strftime("%I:%M %p") #get the time in 12 hour format
    
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10:"October",
        11:"November",
        12:"December"
        } #create a dictionary of months
    
    return f"It is {time} on {now.day} {switcher.get(now.month)} {now.year}" #return the date and time
    