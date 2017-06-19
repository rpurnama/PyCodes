from gtts import gTTS
import os
tts = gTTS(text='Hi Rakhmad, how are you today?', lang='en-us')
tts.save("out.mp3")
os.system("mpg321 out.mp3 -quiet")
