from data.roverData import roverData
import time
import datetime as dt
from matplotlib.pylab import *
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import matplotlib.animation as animation
from numpy import sin, cos
import numpy as np
import math as m


class mainInterface():

    def __init__(self):
        
        self.roverData = roverData()

    def readData(self):
        datos = self.roverData.actData()      # Get random numbers for testing
        return datos
  

# Graficar datos de B
# Initialize communication
mainInterface = mainInterface()

cube = np.array([[-1, -1, -1], [1, -1, -1], [-1, 1, -1], [1, 1, -1]])
X_R = cube[:,0].reshape((2, 2))
Y_R = cube[:,1].reshape((2, 2))
Z_R = cube[:,2].reshape((2, 2))
# # Sent for figure
# font = {'size'   : 9}
# matplotlib.rc('font', **font)

# Setup figure and subplots
# Setup figure and subplots
f0 = plt.figure(num = 0, figsize = (12, 8))#, dpi = 100)
f0.suptitle("Testing", fontsize=12)

ax01 = f0.add_subplot(221)
ax02 = f0.add_subplot(222)
ax03 = f0.add_subplot(223)
ax04 = f0.add_subplot(224, projection='3d')


# Set titles of subplots
ax01.set_title('B vs Time')
ax02.set_title('C vs Time')
ax03.set_title('D vs Time')
ax04.set_title('3D')

# # set y-limits
ax01.set_ylim(0,200)
ax02.set_ylim(400,1200)
ax03.set_ylim(0,200)
ax04.set_ylim(-2,2)

#3D Lables
ax04.axes.xaxis.set_ticklabels([])
ax04.axes.yaxis.set_ticklabels([])
ax04.axes.zaxis.set_ticklabels([])
ax04.set_xlabel("X")
ax04.set_ylabel("Y")
ax04.set_zlabel("Z")

# # sex x-limits
ax01.set_xlim(0,20)
ax02.set_xlim(0,20)
ax03.set_xlim(0,20)
ax04.set_xlim(-7,7)
ax04.set_ylim(-7,7)
ax04.set_zlim(-7,7)

# Turn on grids
ax01.grid(True)
ax02.grid(True)
ax03.grid(True)
ax04.grid(True)

# Data Placeholders
yp1=zeros(0)
yv1=zeros(0)
yv2=zeros(0)
t=zeros(0)

# set plots
p011, = ax01.plot(yp1,t,'b-', label="yp1")
p021, = ax02.plot(yv1,t,'g-', label="yv1")
p031, = ax03.plot(yv2,t,'r-', label="yv2")
ax04.plot_surface(X_R,Z_R,Y_R, color="green", alpha=0.5)
ax04.plot_surface(X_R*-2,Z_R*-2,Y_R*-2, color="red", alpha=0.5)
ax04.view_init(elev = 30, azim=-60)

# Data Update
xmin = 0.0
xmax = 20.0
x = 0.0
y = 30
def updateData(self):

    global x_m, y_m, z_m
    global x
    global y
    global yp1
    global yv1
    global yv2
    global t

    def Rx(theta):
        return np.matrix([[ 1, 0           , 0           ],
                    [ 0, m.cos(theta),-m.sin(theta)],
                    [ 0, m.sin(theta), m.cos(theta)]])
    
    def Ry(theta):
        return np.matrix([[ m.cos(theta), 0, m.sin(theta)],
                    [ 0           , 1, 0           ],
                    [-m.sin(theta), 0, m.cos(theta)]])
    
    def Rz(theta):
        return np.matrix([[ m.cos(theta), -m.sin(theta), 0 ],
                    [ m.sin(theta), m.cos(theta) , 0 ],
                    [ 0           , 0            , 1 ]])


    datos = mainInterface.readData()
    print("test:", datos[0], datos[1], datos[2])

    phi = np.radians(datos[4])
    theta = np.radians(datos[5])
    psi = np.radians(datos[6])
    R = Rz(psi) * Ry(theta) * Rx(phi)

    cube = np.array([[-1, -1, -1], [1, -1, -1], [-1, 1, -1], [1, 1, -1]])
    cube = cube*R
    X_R = cube[:,0].reshape((2, 2))
    Y_R = cube[:,1].reshape((2, 2))
    Z_R = cube[:,2].reshape((2, 2))

    yp1=append(yp1,datos[1])
    yv1=append(yv1,datos[2])
    yv2=append(yv2,datos[3])
    t=append(t,x)

    x += 1

    p011.set_data(t,yp1)
    p021.set_data(t,yv1)
    p031.set_data(t,yv2)

    ax04.cla()
    ax04.axes.xaxis.set_ticklabels([])
    ax04.axes.yaxis.set_ticklabels([])
    ax04.axes.zaxis.set_ticklabels([])
    ax04.set_xlabel("X")
    ax04.set_ylabel("Y")
    ax04.set_zlabel("Z")
    ax04.plot_surface(X_R,Z_R,Y_R, color="green", alpha=0.5)
    ax04.plot_surface(X_R*-2,Z_R*-2,Y_R*-2, color="red", alpha=0.5)
    
    if x >= xmax-1.00:
        p011.axes.set_xlim(x-xmax+1.0,x+1.0)
        p021.axes.set_xlim(x-xmax+1.0,x+1.0)
        p031.axes.set_xlim(x-xmax+1.0,x+1.0)

    return p011, p021, p031
    
simulation = animation.FuncAnimation(f0, updateData, blit=False, frames=200, interval=1000, repeat=False)
plt.show()

#    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
#   plt.show()
