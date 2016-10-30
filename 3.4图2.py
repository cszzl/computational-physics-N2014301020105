# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:40:22 2016

@author: 赵晓胜
"""

import matplotlib.pyplot as plt
import numpy as np
import math

# global var.
g = 9.8
l = 9.8
q = 0.5
OmgD = 2. / 3.


# class Euler
# use Euler METHOD to solve the pendulum
# para. & var.  :    
#             theta0, omg0, t0 - initial angel & angular velocity & time
#             l, g, dt, time - length of string, gravity acceleration, time step size & total time 
#             the time period of this pendulum - 1(s)


class Nonlinear_Cromer(object):
    """docstring for Nonlinear_Cromer"""
    global g, l, q, OmgD
    def __init__(self, _FD = .0, _theta0 = 0.2, _omg0 = .0, _t0 = .0, _dt = 0.04, _time = 8000.):
        self.FD = _FD
        self.theta = [_theta0]
        self.omg = [_omg0]
        self.t = [_t0]
        self.dt = _dt
        self.time = _time
        self.n = int(_time / _dt)
        self.THETA = []
        self.OMG = []
        self.T =[]
# fun. calculate
# n=0 means reset
# n=1 means without reset   
    def calculate(self):
        for i in range(self.n):
            domg = (-(g / l) * math.sin(self.theta[-1]) - q * self.omg[-1] + self.FD * math.sin(OmgD * self.t[-1])) * self.dt
            self.omg.append(self.omg[-1] + domg)
            dtheta = self.omg[-1] * self.dt
            temp_theta = self.theta[-1] + dtheta
            if temp_theta < - math.pi:
                self.theta.append(temp_theta + 2 * math.pi)
            elif temp_theta > math.pi:
                self.theta.append(temp_theta - 2 * math.pi)
            else:
                self.theta.append(temp_theta)
            self.t.append(self.t[-1] + self.dt)
        # print 'theta length:',len(self.theta)


# fun. plotplot_phase_space
#  去除了阶跃点之间的连线的相空间图
    def plot_phase_space(self, _ax, _phi,_lab):
        t = np.array([(i * OmgD - _phi) / np.pi / 2 for i in self.t])
        tempt = np.array([round(i) for i in t])
        tempt2 = t - tempt
        a = []
        for i, j in enumerate(tempt2):
            if abs(j) < 0.001:
                a.append(i)
        self.THETA = [self.theta[i] for i in a]
        self.OMG = [self.omg[i] for i in a]
        # print t, tempt, tempt2,a
        # print a


        _ax.plot(self.THETA, self.OMG, 'o',markersize = 3.3,color = 'g',label = r'$F_D = %.1f, \phi=$' % self.FD + _lab,fontsize=12 )
        # for i in range(len(self.T)-1):
        #     _ax.plot(self.THETA[i+1], self.OMG[i+1], '-', color = _color)



# plot:
#       ax1: theta vs time

fig = plt.figure(figsize = (9.708, 6))
ax1 = fig.add_subplot(221, xlim = (-4, 4))
ax2 = fig.add_subplot(222, xlim = (-4, 4))
ax3 = fig.add_subplot(223, xlim = (-4, 4))
ax4 = fig.add_subplot(224, xlim = (-4, 4))

comp = Nonlinear_Cromer(_FD = 1.2)
comp.calculate()
comp.plot_phase_space(ax1,0,'0')

comp = Nonlinear_Cromer(_FD = 1.2)
comp.calculate()
comp.plot_phase_space(ax2,np.pi / 4,r'$\pi/4$')

comp = Nonlinear_Cromer(_FD = 1.2)
comp.calculate()
comp.plot_phase_space(ax3,np.pi / 2,r'$\pi/2$')

comp = Nonlinear_Cromer(_FD = 1.2)
comp.calculate()
comp.plot_phase_space(ax4, np.pi,r'$\pi$')

for i in fig.axes:
    i.legend(fontsize=12,loc='best')
    # i.set_title(r'$\theta vs time$',fontsize=14)
    i.set_xlabel(r'$\theta (radians)$',fontsize=14)
    i.set_ylabel(r'$\omega (radians/s)$',fontsize=14)
    # i.set_title(r'$Poincare Section$'+r'$(q=\frac{1}{2}, l=g=9.8, \Omega_D=\frac{2}{3})$',fontsize=18)
ax1.text(2,1.2,r'$\omega$'+' '+r'$versus$'+' '+r'$\theta$'+r'$(Poincare Section)$',fontsize=18)
plt.show()