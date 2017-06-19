from espeak import espeak
import os

def ngomong(word):
	#word = ''
	#cmd = espeak -vaf word
	#os.system(cmd)
	espeak.synth(word)
	
kata = raw_input('Say something: ')
ngomong(kata)
