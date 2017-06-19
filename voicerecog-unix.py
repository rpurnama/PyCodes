import speech_recognition as sr
import pyttsx
#import sys,os
import pyaudio


def speak(text):
	speech_engine = pyttsx.init() # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
	speech_engine.setProperty('rate', 150)
	speech_engine.say(text)
	speech_engine.runAndWait()


#recognizer = speech_recognition.Recognizer()
r = sr.Recognizer()

def listen():
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	
	
	try:
		#return r.recognize_sphinx(audio)
		return r.recognize_google(audio)
	except sr.UnknownValueError:
		print("Could not understand audio")
	except sr.RequestError as e:
		print("Recog Error; {0}".format(e))

	return ""

speak('Say something!')
speak('I heard you say'+listen())
