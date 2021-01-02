import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('say somthing')
    audio = r.listen(source)


try :
    print('google thinks what you say ' + r.recognize_google(audio))

except :
    pass
