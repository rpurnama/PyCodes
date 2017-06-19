import random
import sys
import time
import os

def acakDadu(p1, p2):
	comp1 = []
	comp2 = []
	
	#P1 Turn
	print ""
	print "It's time for",p1
	raw_input('Press [Enter] to shake!')
	for i in range(5):
		time.sleep(0.5)
		a = random.randrange(1,6)
		comp1.append(a)
		print comp1[i]		
	print p1,"dice number -->",comp1
	
	#P2 Turn
	print ""
	print "It's time for",p2
	raw_input('Press [Enter] to shake!')
	for i in range(5):
		time.sleep(0.5)
		b = random.randrange(1,6)
		comp2.append(b)		
		print comp2[i]
	print p2,"dice number -->",comp2
	
	print "\nCalculating"
	for x in range(15):
		time.sleep(0.5)
		sys.stdout.write('.')
		sys.stdout.flush()
	print "DONE!"
	time.sleep(0.3)
			
	sumComp1 = sum(comp1)
	sumComp2 = sum(comp2)
	
	if sumComp1 < sumComp2:
		print p1,"total score:",sumComp1,"\t",p2,"total score:",sumComp2
		print p2,"is the Winner.",p1,"is Loose!"
	elif sumComp1 > sumComp2:
		print p1,"total score:",sumComp1,"\t",p2,"total score:",sumComp2
		print p1,"is the Winner.",p2,"is Loose!"
	elif sumComp1 == sumComp2:
		print p1,"total score:",sumComp1,"\t",p2,"total score:",sumComp2
		print "It's Draw!"
	else:
		print sumComp1, sumComp2

print "="*10,"\tWelcome at Battle of Dice","="*10
print "="*10,"\t Throw Your Dice and Win ","="*10
print ""

print """Please Select Game Player: 
\t [1] Single Player
\t [2] Two Player
"""

num_player = raw_input('Your choice: ')

os.system('clear')

if num_player == "1":
	player1 = "COMPUTER"
	player2 = raw_input('Enter your name: ')
	acakDadu(player1,player2)
elif num_player == "2":
	player1 = raw_input('1st Player Name: ')
	player2 = raw_input('2nd Player Name: ')
	acakDadu(player1,player2)
else:
	print "You're selecting wrong number"