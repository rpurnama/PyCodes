import pyttsx

engine = pyttsx.init()
command = raw_input("Enter the Text to Speak: ");
engine.say(command)
engine.runAndWait()

print ("~TT Success~");