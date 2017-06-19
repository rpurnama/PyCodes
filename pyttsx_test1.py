import pyttsx

def bicara(word):
	engine = pyttsx.init()
	engine.setProperty('rate',150)
	engine.say(word)
	engine.runAndWait()

bicara('Hello, what is your name?')
name = raw_input('Input your name: ')

#greetings = 'Hello, how are you?'
bicara('Hello '+name+' how are you?')

