import os

#os.system("espeak 'Hi Sabrina, do you love me?'")
mynameis = raw_input('Enter your name: ')
greeting = 'Hi '+mynameis+', how are you'
os.system("espeak 'greeting'")
