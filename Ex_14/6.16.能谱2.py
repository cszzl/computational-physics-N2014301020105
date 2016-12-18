
"""
Created on Sat Dec 17 20:21:28 2016

@author: 赵晓胜
"""

import numpy as np
import matplotlib.pyplot
from pylab import *
from math import *
import mpl_toolkits.mplot3d

dx=0.01
c=300.0 #speed
dt=dx/c
length=int(1.0/dx)
time=3000
k=1000
y=[[0 for i in range(length)]for n in range(time)]#i represents x, n represents t
#initialize
for i in range(length):
    y[0][i]=exp(-k*(i*dx-0.25)**2)
    y[1][i]=exp(-k*(i*dx-0.25)**2)

r=c*dt/dx
for n in range(time-2):
    for i in range(1,length-1):
        y[n+2][i]=2*(1-r**2)*y[n+1][i]-y[n][i]+r**2*(y[n+1][i+1]+y[n+1][i-1])

figure(figsize=[16,8])
subplot(121)
y5=[]
t=array(range(time))*dt
for n in range(time):
    y5.append(y[n][91])
plot(t,y5,'b',label=r'Observe at 0.10')
xlabel('Time(s)',fontsize=15)
ylabel('Signal',fontsize=15)
xlim(0,0.04)
title('String signal versus time',fontsize=15)
legend(loc='best')
subplot(122)
p=abs(np.fft.rfft(y5))**2
f = np.linspace(0, int(1/dt/2), len(p))
plot(f, p,'r',label='Excited at 25% from the end')
xlim(0,3000)
xlabel('Frequency(Hz)',fontsize=15)
ylabel('Power',fontsize=15)
title('Power spectrum',fontsize=15)
legend(loc='best')
savefig('vibration 6.6 fft 5.png')
show()