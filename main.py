from vpython import *
original_mass = 1500 #飛彈質量
mass_of_earth = 5.9722*10**24 #地球質量
radius = 0.23 #飛彈半徑
radius_of_earth = 6.371 * 10**6 #地球半徑
length = 6.1 #飛彈長度
length_of_warhead = length*3/14.4 #彈頭長度
length_of_missile_body = length*11.4/14.4 #飛彈本體長度
cross_section = radius**2*pi #飛彈橫截面
volume = 1/3*cross_section*length_of_warhead+cross_section*length_of_missile_body #飛彈體積
pushing_force = 1814*1000*(275/2000)**(5/3) #推進力
acceleration_time = 1025*9.8*330/pushing_force #加速時間
drag_force_constant = 0.5 #拖曳力常數
gravitational_constant = 6.6743 * 10 **(-11) #重力常數

center_of_earth = vector(0,0,0) #地球球心
rocket = vector(radius_of_earth,0,0) #火箭
angular_velocity = 2*pi/86400 #地球自轉角速度
h = 0 #火箭離地表高度
omega =  #要換成向量

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

t = 0
dt = 0.0001
while mag(rocket-center_of_earth) >= 0:
    rate(1000)
    m = mass(t)
    RHO = rho(h)
    A = #要做出火箭向量，然後找出截面積
    F = lift(RHO) + drag_force(RHO,v,A) + Coriolis_force(m,omega,v) + gravity(m,h)
    a = F/m
    v += a * dt
    rocket += v * dt
    t += dt

print(rocket)