#Projectile Calculator v0.1
import time
import math

#varibles
v = 0.0
status = 'on'
height = 0.0
weight = 0.0
power = 0.0
mass = 0.0
fudge_factor = 0.0
g = 0.0
pro_area = 0.0
air_density = 0.0
drag = 0.0
vt = 0.0
rnge = 0.0
v_part_one = 0.0
v_part_two = 0.0
u_input = ''
cd = 0.0
units = 'mps'

#intro
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('+                                                      +')
print('+            Ultimate Projectile Calculator            +')
print('+               By Huck Richardson v0.9                +')
print('+     Open Source Theoretical Projectile Calculator    +')
print('+                                                      +')
print('+             A:Scientist  B:Normal  C:Orc             +')
print('+                                                      +')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')



while status == 'on':
	u_input = input()

	if u_input == 'a':
		print('+++++++++++++++++++++++++')
		print('+       Scientist       +')
		print('+++++++++++++++++++++++++')
		print('')
		height = float(input('Please enter your height (m)'))
		weight = float(input('Please enter your weight(kg)'))
		fudge_factor = weight/1000
		mass = float(input('Please enter the mass of the projectile(kg)'))
		power = float(input('Please enter your power output(watts per kilogram)'))
		v_part_one = float(3*height*weight*power)
		v_part_two = float(mass+fudge_factor)
		v = v_part_one/v_part_two
		v = v ** (1/3)
		g = float(input('Please enter the acceleration due to gravity(mps)'))
		air_density = float(input('Please enter the air density (kpm3)'))
		pro_area = float(input('Please enter the cross-sectional-area of the projectile (m)'))
		cd = float((2*mass*g)/(air_density*(v**2)*pro_area))
		vt = float((((2*mass*g)/(pro_area*air_density*cd)))**(1/2))
		rnge = float(v*vt*math.cos(45)/g)
		print('')
		print('You can throw the projectile '+ str(rnge) + ' meters with a top speed of ' + str(v) + ' mps')

	
	elif u_input == 'b':
		print('+++++++++++++++++++++++++')
		print('+         Normal        +')
		print('+++++++++++++++++++++++++')
		print('')
		height = float(input('Please enter your height (m)'))
		weight = float(input('Please enter your weight(kg)'))
		fudge_factor = weight/1000
		mass = float(input('Please enter the mass of the projectile(kg)'))
		print('Please enter your athletic skill')
		print('A:Jelly Man')
		print('B:Average Guy')
		print('C:Pro Althlete')
		u_input = input()
		
		if u_input == 'a':
			power = 5
		
		if u_input == 'b':
			power = 10
			
		if u_input == 'c':
			power = 20
		v_part_one = float(3*height*weight*power)
		v_part_two = float(mass+fudge_factor)
		v = v_part_one/v_part_two
		v = v ** (1/3)
		g = float(9.8)
		air_density = float(1.225)
		pro_area = float(input('Please enter the cross-sectional-area of the projectile'))
		cd = float((2*mass*g)/(air_density*(v**2)*pro_area))	
		vt = float((((2*mass*g)/(pro_area*air_density*cd)))**(1/2))
		rnge = float(v*vt*math.cos(45)/g)
		print('')
		print('You can throw the projectile '+ str(round(rnge,1)) + ' meters with a top speed of ' + str(round(v,1)) + ' mps')
	
	elif u_input == 'c':
		print('+++++++++++++++++++++++++')
		print('+           Orc         +')
		print('+++++++++++++++++++++++++')
		print('')
		height = float(input('Please enter your height (m)'))
		weight = float(input('Please enter your weight(kg)'))
		fudge_factor = float( weight/1000)
		print('Please enter your athletic skill')
		print('A:Jelly Man')
		print('B:Average Guy')
		print('C:Pro Althlete')
		u_input = input()
		
		if u_input == 'a':
			power = 5
		
		if u_input == 'b':
			power = 10
			
		if u_input == 'c':
			power = 20
		
		fudge_factor = weight/1000
		print('Select the projectile you wish to throw')
		print('A:Baseball')
		print('B:Meter Wide Iron Cube')
		print('C:Stapler')
		u_input = input()
			
		if u_input == 'a':
			mass = .14
			pro_area = 0.01
		
		if u_input == 'b':
			mass = 78
			pro_area = 1
		
		if u_input == 'c':
			mass = 0.37
			pro_area = .1
		
		v_part_one = float(3*height*weight*power)
		v_part_two = float(mass+fudge_factor)
		v = v_part_one/v_part_two
		v = v ** (1/3)
		g = float(9.8)
		air_density = float(1.225)
		pro_area = float(0.01)
		cd = float((2*mass*g)/(air_density*(v**2)*pro_area))
		vt = float((((2*mass*g)/(pro_area*air_density*cd)))**(1/2))
		rnge = float(v*vt*math.cos(45)/g)
		print('')
		print('You can throw the projectile '+ str(round(rnge,0)) + ' meters with a top speed of ' + str(round(v,0)) + ' mps')
		
		
#	elif u_input == 'd':
#		print('++++++++++++++++++++++++++++++++++++++++++++++')
#		print('+  A: Change Units ("mps" to "mph")          +')
#		print('+  Other: Check out README in the App files  +')
#		print('+  Read the Starting Screen for options      +')
#		print('++++++++++++++++++++++++++++++++++++++++++++++')
#		u_input = input 
#	
#		if u_input == 'a':
#			u_input = input()
#			if u_input == 'mps':
#				units = 'mps'
#					
#			elif u_input == 'mph':
#				units = 'mph'
#	
#		else:
#			print('')
			
	elif u_input == 'quit':
		quit()
		
	else:
		print('Thats not a valid input. See READ ME, or the Starting Screen for help')