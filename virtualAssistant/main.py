from intent_classification.intent_classification import IntentClassifier #import IntentClassifier class from intent_classification\intent_classification.py
from assistant_functions.weather import get_weather #import get_weather function from assistant_functions\weather.py
from assistant_functions.goodbye import get_goodbye #import get_goodbye function from assistant_functions\goodbye.py
from assistant_functions.greeting import get_greeting #import get_greeting function from assistant_functions\greeting.py
from assistant_functions.dateTime import get_dateTime #import get_dateTime function from assistant_functions\dateTime.py
from assistant_functions.location import get_location #import get_location function from assistant_functions\location.py
import pyttsx3 #import pyttsx library (text to speech)
import speech_recognition as sr #import speech_recognition library (speech to text)

class Assistant:
    
    def __init__(self, name):
        self.name = name #instance variable name
        
        self.speech_engine = pyttsx3.init() #create an instance of pyttsx library
        self.speech_engine.setProperty("rate", 190) #set the rate of the speech to 150 words per minute
        
        self.r = sr.Recognizer() #create an instance of speech_recognition library
        self.mic = sr.Microphone(device_index = 0) #create an instance of Microphone class
        
    def reply(self, text):
        intent = intent_classifier.predict(text) #predict the intent of the text
        
        if intent == "leaving": #check if the intent is leaving and terminate if it is
            self.say(get_goodbye())
            quit()
                    
        replies = {
            "weather": get_weather,
            "leaving": get_goodbye,
            "greeting": get_greeting,
            "dateTime": get_dateTime,
            "location": get_location
            } #create a dictionary of replies
        
        reply_func = replies[intent] #get the function from the dictionary
        
        try:
            if callable(reply_func): #check if the function is callable
                if reply_func == get_greeting:
                    print(reply_func(self))
                    self.say(reply_func(self))
                else:
                    print(reply_func()) #print the reply
                    self.say(reply_func()) #say the reply
                            
        except Exception as e:
            print(f"Error: {e}") #print the error message if there is an error
    
    def say(self, text):
        #uses pyttsx library to convert text to speech
        
        self.speech_engine.say(text) #say the text
        self.speech_engine.runAndWait() #run the speech engine and wait for it to finish        
        
    def listen(self):
        #uses speech_recognition library to convert speech to text
        
        with self.mic as source:
            print("Listening...")
            audio = self.r.listen(source, timeout = 5, phrase_time_limit = 10) #listen to the microphone and store the audio into a variable
            
        return self.r.recognize_google(audio) #return the text from the audio
    
    def main(self):
        #main function of the assistant
        print("Hello!")
        self.say("Hello!")
        
        while True:
            said = self.listen() #listen to the microphone and store the text into a variable
            print(said)
            self.reply(said) #reply to the text
            
        
assistant = Assistant("Sylvie") #create an instance of Assistant class and passing name variable into it
intent_classifier = IntentClassifier() #create an instance of IntentClassifier class
assistant.main()