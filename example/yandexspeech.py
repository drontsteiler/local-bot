import speech_recognition as sr
from os import path


def rec(filename=None, bytes=None):
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), filename)
    r = sr.Recognizer()
    txt = "Begin"

    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)

    try:
        txt = "You  said: " + r.recognize_google(audio, language="ru_RU")
    except sr.UnknownValueError:
        txt = "Google Speech Recognation could not understand audio"
    except sr.RequestError as e:
        txt = "Could not request results from Google Speech Recognation service; {0}".format(e)

    return txt


print(rec(filename="test01.mp3"))

""" if filename:
     with open(filename, 'br') as file:
         bytes = file.read()
 if not bytes:
     raise Exception('Neither file name nor bytes provided.')
"""

"""
with sr.Microphone() as source:
    print("Speak anything:")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio,language="ru_RU")
        print("You said: {}".format(text))

    except:
        print("Sorry could not recognize your voice !")
"""
