# Polygon excercise from Week 0

# Name: Tharathorn Rimchala

from TurtleWorld import * 		

# This is where you put code to move bob
def square(bob,l):				
	for i in range(4):
		fd(bob,l)
		rt(bob)

def polygon(bob,l,n):
	drawarc(bob,n,l,n)
	#for i in range(n):
	#	fd(bob,l)
	#	lt(bob,360/n)

def circle(bob,r):
	arc(bob,r,360)
	# from math import pi
	# # circumference length
	# L = 2*pi*r
	# # number of side
	# n = 36
	# # draw it
	# drawarc(bob,n,L/n,n)

def arc(bob,r,theta):
		from math import pi
		fr = theta/360.0
		# n2 - number of sides of equivalent closed polygon
		n2 = 36
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
		rt(bob,360/n2)

def circle2(bob,r,theta):
	
	from math import pi
	n = 36
	# number of side
	# ns = arc(theta)
	# segment length
	l = 2*pi*r/n
	# draw it
	polygon(bob,l,n)
	
# Main script	
world = TurtleWorld()			
bob = Turtle()
l = 50
n = 6
r = 25
theta = 360
# Exercise 2.1
square(bob,l)
# Exercise 2.2
polygon(bob,l,n)
# Exercise 2.3
circle(bob,r)
# Exercise 2.4
arc(bob,2*r,theta)

wait_for_user()					
