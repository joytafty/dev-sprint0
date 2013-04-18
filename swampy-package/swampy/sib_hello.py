# Hello excercise from Week 0

# Name:


from TurtleWorld import * 		
world.clear()
bob = Turtle()

w = 25
h = 50
sp = 10

# %%% Draw H 
# first vstroke
rt(bob)
fd(bob,h)
# transfer turtle
bk(bob,0.5*h)
lt(bob)
# hstroke
fd(bob,w)
# transfer turtle
pu(bob)
rt(bob)
bk(bob,0.5*h)
# vstroke 2
pd(bob)
fd(bob,h)
pu(bob)

# %%% Draw E
# transfer turtle
lt(bob)
fd(bob,sp)
lt(bob)
pd(bob)
# vstroke 
fd(bob,h)
rt(bob)
# hstroke
fd(bob,w)
# transfer turtle
pu(bob)
rt(bob)
fd(bob,0.5*h)
# hstroke top
pd(bob)
rt(bob)
# hstroke middle
fd(bob,w)
lt(bob)
fd(bob,0.5*h)
lt(bob)
# hstroke bottom
fd(bob,w)
pu(bob)

# %%% Draw L1
# transfer turtle
fd(bob,sp+w)
pd(bob)
# hstroke
bk(bob,w)
lt(bob)
# vstroke
fd(bob,h)
pu(bob)

# %%% Draw L2
# transfer turtle
rt(bob)
fd(bob,w+sp)
rt(bob)
pd(bob)
# vstroke
fd(bob,h)
lt(bob)
# hstroke
fd(bob,w)
pu(bob)

# %%% Draw O
# Transfer turtle
fd(bob,sp)
pd(bob)
# hstroke bottom
fd(bob,w)
lt(bob)
# vstroke right
fd(bob,h)
lt(bob)
# hstroke top
fd(bob,w)
lt(bob)
# vstroke left
fd(bob,h)


wait_for_user()					
