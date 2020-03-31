import speech_recognition as sr
import pyaudio

sr.Microphone(device_index=1)

r=sr.Recognizer()

r.energy_threshold=5000

with sr.Microphone() as source:
    print("speak anything")
    audio=r.listen(source)
    try:     
        text=r.recognize_google(source)
        print("you said :{}".format(text))
    except:
        print("sorry coudnt recognise your voice")
