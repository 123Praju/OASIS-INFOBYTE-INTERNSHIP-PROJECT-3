import pyttsx3 as pyt #to convert text to speech
import speech_recognition as spr #use to recognize speech
from selenium_web import InfoW
from youtube_web import youtube_vid
from news_web import *
from weather import *
from datetime import datetime
from my_email import send_email


engine = pyt.init() 

rate=engine.getProperty('rate') # speed of assistant speaking
engine.setProperty('rate',160) #set speed of assistant speaking

voices=engine.getProperty('voices') #shows types of voices
engine.setProperty('voice',voices[1].id) #set type of assistant voice
# print(voices)

def speak(text):
    engine.say(text) #for assistant speaking 
    engine.runAndWait()

def wishme():
    hour=int(datetime.now().hour)
    if hour>0 and hour<12:
        return("Good Morning")
    elif hour>=12 and hour<16:
        return("Good Afternoon")
    else:
        return("Good Evening")


r = spr.Recognizer() #Use to retrive the audio from microphone

speak("Hello! Today is {}, {} {} {}, and its currently {}:{} {}".format(datetime.now().strftime("%A"),datetime.now().strftime("%B"),datetime.now().strftime("%d"),datetime.now().strftime("%Y"),datetime.now().strftime("%I"),datetime.now().strftime("%M"),datetime.now().strftime("%p")))
speak("Todays temprature in India is "+str(temp())+"degree celsius , with"+str(des()))
speak(wishme() + ", I am your personal assistant. How are you?")

with spr.Microphone() as source:
    r.energy_threshold=10000 #audio frequency
    r.adjust_for_ambient_noise(source,1.2)
    print("Listning...")
    audio = r.listen(source) #Listen voice words
    text = r.recognize_google(audio) #convert voice into text
    print(text)

if "what" and "about" and "you" in text:
    speak("I am totally fine. Thank you!")
speak("How can I help you ?")


with spr.Microphone() as source:
    r.energy_threshold=10000 #audio frequency
    r.adjust_for_ambient_noise(source,1.2)
    print("Listning...")
    audio = r.listen(source) #Listen voice words
    text2 = r.recognize_google(audio) #convert voice into text
    print(text2)

if "information" in text2 :
    speak("You need information related to which topic ?")

    with spr.Microphone() as source:
        r.energy_threshold=10000 #audio frequency
        r.adjust_for_ambient_noise(source,1.2)
        print("Listning...")
        audio = r.listen(source) #Listen voice words
        infor = r.recognize_google(audio) #convert voice into text
        print(infor)

# Create an instance of the InfoW class and perform a search
    assist = InfoW(speak)            #selenium_web.InfoW()
    assist.get_info(infor)

elif "video" in text2 or "play" in text2 :
    speak("You need video related to which topic ?")

    with spr.Microphone() as source:
        r.energy_threshold=10000 #audio frequency
        r.adjust_for_ambient_noise(source,1.2)
        print("Listning...")
        audio = r.listen(source) #Listen voice words
        infor = r.recognize_google(audio) #convert voice into text
        print(infor)

# Create an instance of the youtube_vid class and perform a search
    assist = youtube_vid()
    assist.play(infor)

elif "news" in text2 : 
    speak("Sure...")
    nws=news()
    for i in range(len(nws)):
        print(nws[i])
        speak(nws[i]) 

elif "email" in text2:
    speak("Sure, please provide the recipient's email address.")

    with spr.Microphone() as source:
        r.energy_threshold = 10000  # audio frequency
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)  # Listen voice words
        recipient_email = r.recognize_google(audio)  # convert voice into text
        print(recipient_email)

    speak("What is the subject of the email?")

    with spr.Microphone() as source:
        r.energy_threshold = 10000  # audio frequency
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)  # Listen voice words
        email_subject = r.recognize_google(audio)  # convert voice into text
        print(email_subject)

    speak("what is the content of the email.")

    with spr.Microphone() as source:
        r.energy_threshold = 10000  # audio frequency
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)  # Listen voice words
        email_content = r.recognize_google(audio)  # convert voice into text
        print(email_content)

    send_email(recipient_email, email_subject, email_content)
    speak("The email has been sent successfully.")
