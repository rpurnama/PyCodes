import os

try:
	myfile = open("passdict.txt",'a')

	password = raw_input('Please enter your password: ')			
	myfile.writelines(password+'\n')
	myfile.close()
except IOError,e:
	print "Application Error",e
