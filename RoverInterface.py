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
import random

frequency = 100 # code frequency in ml seconds


class mainInterface():

    def __init__(self):
        
        self.roverData = roverData()
        self.n = 0

    def readData(self):
        data = self.roverData.actData()
        A = self.n
        self.n += 1  
        B, C, D, E, F, G, H, I = data
        datos = {'Time': A, 'Temperature': B, 'Pressure': C, 'Altitude': D,\
                    'Latitude': E, 'Longitude': F, 'Roll': G, 'Pitch': H, 'Yaw': I}    
        return datos
  

# Graficar datos de B
# Initialize communication
mainInterface = mainInterface()

# # Sent for figure
# font = {'size'   : 9}
# matplotlib.rc('font', **font)

# Setup figure and subplots
# Setup figure and subplots
f0 = plt.figure(num=0, figsize=(12, 8))#, dpi = 100)
f0.suptitle("Interface", fontsize=12)

ax01 = f0.add_subplot(221)
ax02 = f0.add_subplot(222)
ax03 = f0.add_subplot(223)
ax04 = f0.add_subplot(224, projection='3d')


# Set titles of subplots
ax01.set_title('Climate Data')
ax02.set_title('Preassure')

# # set y-limits
ax01.set_ylim(0, 120)
ax02.set_ylim(400, 1200)

# # sex x-limits
ax01.set_xlim(0, 20)
ax02.set_xlim(0, 20)

# Turn on grids
ax01.grid(True)
ax02.grid(True)

# Data Placeholders
yp11 = zeros(0) # Temperature
yp12 = zeros(0) # Altitude
yp21 = zeros(0) # Pressure
t = zeros(0)

# set plots
p011, = ax01.plot(yp11, t, 'red', label="Temperature: ºC")
p012, = ax01.plot(yp12, t, color="blue", label="Altitude: meters")
p021, = ax02.plot(yp21, t, 'green', label="Pressure: hPa")

ax04.view_init(elev=20, azim=130)

# Data Update
start = True
xmin = 0.0
xmax = 20.0
x = 0.0

# Map Position
map_range = 100
x_initial = 0 #datos.get('Latitude')
y_initial = 0 #datos.get('Longitude')
x_llim = 0
x_hlim = 0
y_llim = 0
y_hlim = 0


def updateData(self):
    
    global start
    global x
    global y
    global yp11, yp12, yp13
    global yp21
    global t
    global x_initial, y_initial
    global x_llim, x_hlim 
    global y_llim, y_hlim 

    def Rx(theta):
        return np.matrix([[1, 0, 0],
                    [0, m.cos(theta), -m.sin(theta)],
                    [0, m.sin(theta), m.cos(theta)]])
    
    def Ry(theta):
        return np.matrix([[m.cos(theta), 0, m.sin(theta)],
                    [0, 1, 0],
                    [-m.sin(theta), 0, m.cos(theta)]])
    
    def Rz(theta):
        return np.matrix([[m.cos(theta), -m.sin(theta), 0],
                    [m.sin(theta), m.cos(theta), 0],
                    [0, 0, 1]])

    datos = mainInterface.readData()

    phi = np.radians(datos.get('Roll'))
    theta = np.radians(datos.get('Pitch'))
    psi = np.radians(datos.get('Yaw'))
    R = Rz(psi) * Ry(theta) * Rx(phi)

    face = np.array([[-2, -2, -2], [2, -2, -2], [-2, -2, 2], [2, -2, 2]])
    face = face * R
    X_R = face[:, 0].reshape((2, 2))
    Y_R = face[:, 1].reshape((2, 2))
    Z_R = face[:, 2].reshape((2, 2))

    face2 = face[[2, 3], :]
    face2 = np.vstack((face2, face2 * .5))
    X_R2 = face2[:, 0].reshape((2, 2))
    Y_R2 = face2[:, 1].reshape((2, 2))
    Z_R2 = face2[:, 2].reshape((2, 2))

    face3 = face[[0, 2], :]
    face3 = np.vstack((face3, face3 * .5))
    X_R3 = face3[:, 0].reshape((2, 2))
    Y_R3 = face3[:, 1].reshape((2, 2))
    Z_R3 = face3[:, 2].reshape((2, 2))

    face4 = face[[0, 1], :]
    face4 = np.vstack((face4, face4 * .5))
    X_R4 = face4[:, 0].reshape((2, 2))
    Y_R4 = face4[:, 1].reshape((2, 2))
    Z_R4 = face4[:, 2].reshape((2, 2))

    face5 = face[[1, 3], :]
    face5 = np.vstack((face5, face5 * .5))
    X_R5 = face5[:, 0].reshape((2, 2))
    Y_R5 = face5[:, 1].reshape((2, 2))
    Z_R5 = face5[:, 2].reshape((2, 2))

    yp11 = append(yp11, datos.get('Temperature'))
    yp12 = append(yp12, datos.get('Altitude'))
    yp21 = append(yp21, datos.get('Pressure'))
    t = append(t, x)

    x += 1

    p011.set_data(t, yp11)
    p012.set_data(t, yp12)
    ax01.legend()
    p021.set_data(t, yp21)
    ax02.legend()

    if start:
        x_initial = 0 #datos.get('Latitude')
        y_initial = 0 #datos.get('Longitude')
        x_llim = x_initial - map_range
        x_hlim = x_initial + map_range
        y_llim = y_initial - map_range
        y_hlim = y_initial + map_range
        start = False
    ax03.cla()
    ax03.scatter(x_initial, y_initial, color='green', label="Initial Position", alpha=0.5)
    ax03.scatter(datos.get('Latitude'), datos.get('Longitude'),\
        color='red', label="Actual Position", alpha=0.3)
    ax03.set_xlim(x_llim, x_hlim)
    ax03.set_ylim(y_llim, y_hlim)
    ax03.set_xlabel('X (meters)')
    ax03.set_ylabel('Y (meters)')
    ax03.legend()

    ax04.cla()

    ax04.set_title('Roll, Pitch and Yaw')
    ax04.axes.xaxis.set_ticklabels([])
    ax04.axes.yaxis.set_ticklabels([])
    ax04.axes.zaxis.set_ticklabels([])
    ax04.set_xlabel("X")
    ax04.set_ylabel("Y")
    ax04.set_zlabel("Z")
    ax04.plot_surface(X_R * .5, Y_R * .5, Z_R * .5, color="blue", alpha=.7)
    ax04.plot_surface(X_R, Y_R, Z_R, color="yellow", alpha=.3)
    ax04.plot_surface(X_R2, Y_R2, Z_R2, color="green", alpha=.7)
    ax04.plot_surface(X_R3, Y_R3, Z_R3, color="yellow", alpha=.3)
    ax04.plot_surface(X_R4, Y_R4, Z_R4, color="yellow", alpha=.3)
    ax04.plot_surface(X_R5, Y_R5, Z_R5, color="yellow", alpha=.3)

    ax04.set_ylim(-2.5, 2.5)
    ax04.set_xlim(-2.5, 2.5)
    ax04.set_zlim(-2.5, 2.5)
    
    if x >= xmax - 1.00:
        p011.axes.set_xlim(x - xmax + 1.0, x + 1.0)
        p021.axes.set_xlim(x - xmax + 1.0, x + 1.0)

    return p011, p021


simulation = animation.FuncAnimation(f0, updateData, blit=False, interval=frequency, repeat=False)
plt.show()

#    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
#   plt.show()
