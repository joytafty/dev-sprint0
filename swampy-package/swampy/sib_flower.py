# Flower excercise (4.2) from Week 0

# Name: Tharathorn Rimchala

def arc(bob,r,theta):
		from math import pi
		fr = theta/360.0
		# n2 - number of sides of equivalent closed polygon
		n2 = 72
		# n1 - number of sides to draw
		n1 = int(round(fr*n2))
		L = 2*pi*r	
		drawarc(bob,n1,L/n2,n2)

def drawarc(bob,n1,l,n2):
	# n1 - number of sides to draw
	# l - segment length
	# n2 - number of sides of equivalent closed polygon
	for i in range(n1):
		fd(bob,l)
		lt(bob,360/n2)

def flower(bob,n,r,theta):
	thetaturn = 360.0/n
	for i in range(n):
		drawpetal(bob,n,r,theta)
		lt(bob,thetaturn)

def drawpetal(bob,n,r,theta):
	for i in range(2):
		arc(bob,r,theta)
		lt(bob,180-theta)

# Main script

from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				

# This is where you put code to move bob
# Exercise 4.2
theta1 = 60.0
r1 = 60.0
npetal1 = 7
# Draw first flower in 4.1
flower(bob,npetal1,r1,theta1)

# Transfer turtle
pu(bob)
fd(bob, 3*r1)
pd(bob)

# Draw second flower in 4.1
theta2 = 80.0
r2 = 40.0
npetal2 = 10
flower(bob,npetal2,r2,theta2)

# Transfer turtle
pu(bob)
fd(bob, 3*r1)
pd(bob)

# Draw second flower in 4.3
theta3 = 20.0
r3 = 140.0
npetal3 = 20
flower(bob,npetal3,r3,theta3)

wait_for_user()					

