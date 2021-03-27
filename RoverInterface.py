from data.roverData import roverData
import time
import datetime as dt
import numpy
from matplotlib.pylab import *
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
from mpl_toolkits import mplot3d
import matplotlib.animation as animation
from mpl_toolkits import mplot3d

class mainInterface():

    def __init__(self):
        
        self.roverData = roverData()

    def readData(self):
        datos = self.roverData.actData()      # Get random numbers for testing
        return datos
  

if __name__ == "__main__":
    # Graficar datos de B
    # Initialize communication
    mainInterface = mainInterface()

    # # Sent for figure
    # font = {'size'   : 9}
    # matplotlib.rc('font', **font)
    
    # Parameters
    x_len = 200         # Number of points to display
    y_range = [10, 40]  # Range of possible Y values to display

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

    # # set y-limits
    ax01.set_ylim(0,200)
    ax02.set_ylim(400,1200)
    ax03.set_ylim(0,200)

    # # sex x-limits
    ax01.set_xlim(0,10.0)
    ax02.set_xlim(0,10.0)
    ax03.set_xlim(0,5.0)

    # Turn on grids
    ax01.grid(True)
    ax02.grid(True)
    ax03.grid(True)

    # Data Placeholders
    yp1=zeros(0)
    yv1=zeros(0)
    yv2=zeros(0)
    t=zeros(0)

    # set plots
    p011, = ax01.plot(yp1,t,'b-', label="yp1")

    p021, = ax02.plot(yv1,t,'g-', label="yv1")

    p031, = ax03.plot(yv2,t,'r-', label="yv2")

    # Data Update
    xmin = 0.0
    xmax = 5.0
    x = 0.0

    def updateData(self):
        global x
        global yp1
        global yv1
        global yv2
        global t

        datos = mainInterface.readData()
        print("test:", datos[0], datos[1], datos[2])

        yp1=append(yp1,datos[1])
        yv1=append(yv1,datos[2])
        yv2=append(yv2,datos[3])
        t=append(t,x)

        x += 1

        p011.set_data(t,yp1)

        p021.set_data(t,yv1)

        p031.set_data(t,yv2)

        if x >= xmax-1.00:
            p011.axes.set_xlim(x-xmax+1.0,x+1.0)
            p021.axes.set_xlim(x-xmax+1.0,x+1.0)
            p031.axes.set_xlim(x-xmax+1.0,x+1.0)

        return p011, p021, p031

    
        
    simulation = animation.FuncAnimation(f0, updateData, blit=False, frames=200, interval=1000, repeat=False)
    plt.show()
        
        

#    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
#   plt.show()
