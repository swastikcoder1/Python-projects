#this project has only 4 functions. If you loke you may add other fumctions like play ing music from your pc
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime #pip install datetime
import pywhatkit #pip install pywhatkit
import wikipedia #pip install wikipedia
import webbrowser #pre-installed module

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 145)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak(" ")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("please say again")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        if 'help' in query:
            speak('sir, please say me how may i help you')
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'google' in query:
            webbrowser.open("https://www.google.com")

        elif 'google meet' in query:
            webbrowser.open("https://meet.google.com")
        
        elif 'search' in query:
            speak('Searching ')
            query = query.replace("search", "")
            results = pywhatkit.search(query)
        elif 'exit' in query:
            exit()
          