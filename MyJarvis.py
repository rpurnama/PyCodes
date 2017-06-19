import time
import getpass
import sys

print """
       db   d8b   db d88888b db       .o88b.  .d88b.  .88b  d88. d88888b 
       88   I8I   88 88'     88      d8P  Y8 .8P  Y8. 88'YbdP`88 88'     
       88   I8I   88 88ooooo 88      8P      88    88 88  88  88 88ooooo 
       Y8   I8I   88 88ooooo 88      8b      88    88 88  88  88 88ooooo 
       `8b d8'8b d8' 88.     88booo. Y8b  d8 `8b  d8' 88  88  88 88.     
        `8b8' `8d8'  Y88888P Y88888P  `Y88P'  `Y88P'  YP  YP  YP Y88888P 
\t================================================================
\tProgrammed by rpurnama for personal usage. This program is still 
\tunder development, it isn't for commercial purpose. So, please 
\tuse with your own risk. (c) RPOERNAMA Corporation.
"""

id_login = raw_input('User ID: ')
#id_login = "Please Enter Your Identification!"
pass_login = getpass.getpass('Password: ')
#print(pass_login)

def Jarvis(feedback):
	if feedback != '':
		if "who are you" in feedback:
			print("My name is Jarvis, nice to see you!")
		elif "exit" in feedback:
			print("System Closed. Good Bye!")
			sys.exit(0)
		else:
			print("I don\'t understand you")
	else:
		pass
		
time.sleep(1)
while True:
	inpdata = raw_input('What\'s your command: ')
	Jarvis(inpdata)