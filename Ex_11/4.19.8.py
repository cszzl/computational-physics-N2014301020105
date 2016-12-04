# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 18:53:29 2016

@author: 赵晓胜
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 16:16:43 2016

@author: 赵晓胜
"""

import numpy as np
from pylab import *
from math import *
import mpl_toolkits.mplot3d

def Hyperion(theta0):
    x=[]
    x.append(1)
    v_x=[]
    v_x.append(0)
    y=[]
    y.append(0)
    v_y=[]
    v_y.append(2*pi)
    
    omega=[]
    omega.append(0)
    theta=[]
    theta.append(theta0)
    t=[]
    t.append(0)
    time=20.0
    dt=0.0001
    for i in range(int(time/dt)):
        r=sqrt(x[i]**2+y[i]**2)
        v_x.append(v_x[i]-4*pi**2*x[i]*r**(-3)*dt)
        x.append(x[i]+v_x[i+1]*dt)
        v_y.append(v_y[i]-4*pi**2*y[i]*r**(-3)*dt)
        y.append(y[i]+v_y[i+1]*dt)
        
        omega.append(omega[i]-dt*12*pi**2*r**(-5)*(x[i]*sin(theta[i])-y[i]*cos(theta[i]))*(x[i]*cos(theta[i])+y[i]*sin(theta[i])))

        theta_new=theta[i]+omega[i+1]*dt
        while theta_new > pi:
            theta_new -= 2*pi
        while theta_new < -pi:
            theta_new += 2*pi
        theta.append(theta_new)
        t.append(t[i]+dt)
    return [theta,omega,t,x,y]
H0=Hyperion(0)
theta=H0[0]
omega=H0[1]
t=H0[2]
x=H0[3]
y=H0[4]
H1=Hyperion(0.01)
dtheta=np.array(H1[0])-np.array(H0[0])
#plot
figure(figsize=[4,4])
plot(x,y)
xlim(-2.5,2.5)
ylim(-3.5,3.5)
scatter(0,0,s=50,color='red')
show()
figure(figsize=[12,8])
subplot(121)
plot(t,theta,'g')
title('Hyperion $\\theta$ versus time',fontsize=15)
xlabel('time(yr)')
ylabel('$\\theta$(radians)')
xlim(0,8)
ylim(-4,4)
subplot(122)
plot(t,omega,'g')
title('Hyperion $\\omega$ versus time',fontsize=15)
xlabel('time(yr)')
ylabel('$\\omega$(radians/yr)')
savefig('Hyperion.png')
xlim(0,8)
ylim(0,15)
show()

plot(t,dtheta)
title('Hyperion $\\Delta$$\\theta$ versus time',fontsize=15)
xlabel('time(yr)')
ylabel('$\\Delta\\theta$(radians)')
savefig('Hyperion dtheta.png')
xlim(0,10)
ylim(0.0001,10)
show()