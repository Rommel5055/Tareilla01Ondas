from visual import*
from visual.graph import*
from math import*

funct1 = gcurve(color=color.cyan)
funct2 = gcurve(color=color.red)
funct3 = gcurve(color= color.green)

display(width=800,height=800,center=vector(6,0,0),background=color.white)
wall=box(pos=vector(0,1,0),size=vector(0.2,3,2),color=color.green)

Mass1=box(pos=vector(1.1,0,0),velocity=vector(2,0,0),size=vector(1,1,1),mass=4.0,color=color.blue)
pivot=vector(0,0,0)
spring1=helix(pos=pivot,axis=Mass1.pos-pivot,radius=0.4,constant=400000,thickness=0.1,coils=20,color=color.red)
eq=vector(1,0,0)

Mass2=box(pos=vector(2.1,0,0),velocity=vector(-2,0,0),size=vector(1,1,1),mass=4.0,color=color.blue)
spring2=helix(pos=Mass1.pos,axis=Mass2.pos-Mass1.pos,radius=0.4,constant=400000,thickness=0.1,coils=20,color=color.red)

w1 = 195.4395075848547956004775038307885929564402118779761769512
w2 = 511.6672736016927288003668582740604463283957258104978596370

v1 = float((1+sqrt(5))/2)
v2 = float((1-sqrt(5))/2)

C = (1.1*v1 - 2.1)/(1-v2)
A = 1.1 - C

#C = 0.143181
#A = 1.1 - C

D = ((2*w1*(v1))+(2+C+A))/((w1*w2*v1) - (w2*v2))
B = (2 - D*w2)/w1

print A*v1+C*v2
print A + C

print "A = " + str(A)
print "B = " + str(B)
print "C = " + str(C)
print "D = " + str(D)

t=0
dt=0.01
while (t<0.1):
	rate(100)
	

	Mass1.velocity=vector((((w1*(-A *sin (w1*t))) + (w1*(B * cos(w1*t)))) + ((w2*(-C*sin(w2*t))) + (w2*(D*cos(w2*t))))),0,0)
	Mass1.pos=vector((((A *cos (w1*t)) + (B * sin(w1*t))) + ((C*cos(w2*t)) + (D*sin(w2*t)))),0,0)
	spring1.axis=Mass1.pos-spring1.pos

	Mass2.velocity = vector(( ( (-A *sin (w1*t)) + (B * cos(w1*t)))*(v1)*(w1) + ((A *cos (w1*t)) + (B * sin(w1*t))) + ((-C*sin(w2*t)) + (D*cos(w2*t)))*(v2)*(w2) + ((C*cos(w2*t)) + (D*sin(w2*t))) ),0,0)
	Mass2.pos = vector((((A *cos (w1*t)) + (B * sin(w1*t)))*(v1) + ((C*cos(w2*t)) + (D*sin(w2*t)))*v2),0,0)
	spring2.pos = Mass1.pos
	spring2.axis = Mass2.pos-Mass1.pos



	funct1.plot(pos=(t,Mass1.pos.x))
	funct2.plot(pos=(t,Mass2.pos.x))
	#funct3.plot(pos=(t,(Mass2.pos.x + Mass1.pos.x)/2))

	t=t+dt

#http://techforcurious.website/simulation-of-spring-mass-system-vpython-tutorial-visual-python/
