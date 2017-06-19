#While looping
import sys
import time

kursor = ['|','/','-','\\']
i = 0


while (i<50):
	for a in range(1, 4):
		b = kursor[a]
		sys.stdout.write("\r%s" %b)
		sys.stdout.flush()
		time.sleep(0.01)
	
	i+=1
	
		
