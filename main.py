from vpython import *
original_mass = 1500
mass_of_earth = 5.9722*10**24
radius = 0.23
radius_of_earth = 6.371 * 10**6
length = 6.1
length_of_warhead = length*3/14.4
length_of_missile_body = length*11.4/14.4
cross_section = radius**2*pi
volume = 1/3*cross_section*length_of_warhead+cross_section*length_of_missile_body
pushing_force = 1814*1000*(275/2000)**(5/3)
acceleration_time = 1025*9.8*330/pushing_force
drag_force_constant = 0.5
gravitational_constant = 6.6743 * 10 **(-11)

g = 9.8
def mass(t):
    if t < acceleration_time:
        return original_mass-1025*t/acceleration_time
    else:
        return 475
def rho(h):
    if h > 25000:
        T = -131.21 + 0.00299*h
        p = 2.488 * ((T+273.1)/216.6)**(-11.388)
    elif 25000 >= h > 11000:
        T = -56.46
        p = 22.65*e**(1.73-0.000157*h)
    else:
        T = 15.04-0.00649*h
        p = 101.29*((T+273.1)/288.08)**(5.256)
    rho = p/(0.2869*(T+273.1))
    
def lift(rho):
    # something went wrong (Bernoulli's Principle)
    return rho*volume*g + rho*g 
def drag_force(rho,v,A):
    return 0.5*rho*drag_force_constant*v**2*A
def Coriolis_force(mass,omega,v):
    # something went wrong (omega)
    # something went wrong (v)
    return -2*mass*cross(omega,v)
def gravity(mass,h):
    return - gravitational_constant*mass_of_earth*mass/(h+radius_of_earth)**2