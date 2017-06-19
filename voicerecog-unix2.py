import speech_recognition as sr
import os
import pyaudio
from gtts import gTTS

#speech_engine = pyttsx.init() # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
#speech_engine.setProperty('rate', 150)

"""
def speak(text):
	speech_engine.say(text)
	speech_engine.runAndWait()
"""
def ngomong(kata):
	tts = gTTS(kata,lang='en')
	tts.save('output.mp3')
	os.system('mpg321 output.mp3 -quiet')	


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

ngomong("Hello, what's your name?")
mynameis = raw_input('Enter your name: ')
ngomong("How are you "+mynameis)
#ngomong("How are you "+listen())

#speak('Who are you?')
#speak('Hi ' + mynameis)
#speak('How are you?')

#speak('Say something!')
#speak('I heard you say'+listen())


