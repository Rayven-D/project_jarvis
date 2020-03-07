import speech_recognition as sr
import pyttsx3

r =sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')
speech_rate = engine.getProperty('rate')
engine.setProperty('rate', speech_rate-25)

user_string = ''
while True:
    with sr.Microphone() as trigger_source:
        r.adjust_for_ambient_noise(trigger_source)
        audio = r.listen(trigger_source)
        if(r.recognize_google(audio)== "Earth"):
            break;

while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Hello, how should I help you today?")
        engine.say('Hello, how should I help you today?')
        engine.runAndWait()
        audio = r.listen(source)

    try:
        user_string += r.recognize_google(audio)
    except sr.UnknownValueError:
        continue;
    except sr.RequestError as e:
        print("Could not request results".format(e))
        exit(0);
    if('stop' in user_string or 'exit' in user_string):
        break;