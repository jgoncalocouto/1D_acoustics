import matplotlib.pyplot as plt
import math
import numpy as np
import speedtest
from datetime import datetime

download_list=[]

t_step=0.001; #[s]
t_total=1; #[h]
c=341
x_step=0.1
l=c/5
P_source=20;
f_source=20
w=2*math.pi*(f_source)
phi=math.pi/4
rho=1.2

t=np.arange(0,t_total,t_step)
x=np.arange(0,l,x_step)
p=np.zeros((math.ceil(t_total/t_step),math.ceil(l/x_step)))
v=np.zeros((math.ceil(t_total/t_step),math.ceil(l/x_step)))

for xi in range(len(x)):
    for ti in range(len(t)):
        p[ti,xi]=math.cos(-w*x[xi]/c+w*t[ti])*P_source
        #v[ti,xi]=(math.sin(w*x[xi]/c)*((P_source)/(rho*c))*math.sin(w*t[ti]+phi))*100


ax = plt.axes(xlim=(0, l), ylim=(-P_source-1, P_source+1))
line, = plt.plot(t,p[:,0],'k-')
line2,=plt.plot(t,v[:,0],'r-')

plt.ion()
plt.show()
plt.xlabel('x - [m]')
plt.ylabel('Pressure Wave- [Pa]')

for ti in range(len(t)):
    line.set_xdata(x)
    line.set_ydata(p[ti,:])
    line2.set_xdata(x)
    line2.set_ydata(v[ti,:])
    plt.draw()
    plt.pause(t_step)

