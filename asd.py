
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos
from itertools import product, combinations
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("auto")
ax.set_autoscale_on(True)


#dibujar punto
#ax.scatter([0],[0],[0],color="g",s=100)

d = [-2, 2]

for s, e in combinations(np.array(list(product(d,d,d))), 2):
    if np.sum(np.abs(s-e)) == d[1]-d[0]:
        ax.plot3D(*zip(s,e), color="g")

theta = np.radians(30)
for s, e in combinations(np.array(list(product(d,d,d))), 2):
    if np.sum(np.abs(s-e)) == d[1]-d[0]:
        s_rotated = [s[0] * cos(theta) - s[1] * sin(theta), 
                     s[0] * sin(theta) + s[1] * cos(theta),
                     s[2]]
        e_rotated = [e[0] * cos(theta) - e[1] * sin(theta), 
                     e[0] * sin(theta) + e[1] * cos(theta),
                     e[2]]      
        print(s_rotated, e_rotated)
        ax.plot3D(*zip(s_rotated,e_rotated), color="g")
"""
#plt.show()

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from numpy import sin, cos
import numpy as np
import math as m
  
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

phi = np.radians(0)
theta = np.radians(0)
psi = np.radians(0)

R = Rz(psi) * Ry(theta) * Rx(phi)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

cube = np.array([[-1, -1, -1], [1, -1, -1], [-1, 1, -1], [1, 1, -1]])

#x = cube[:,0].reshape((2, 2))
"""
cube[0,:] = cube[0,:]*R
cube[1,:] = cube[1,:]*R
cube[2,:] = cube[2,:]*R
cube[3,:] = cube[3,:]*R
"""
#print(cube[1,:])
cube = cube*R
#print(cube)

X_R = cube[:,0].reshape((2, 2))
Y_R = cube[:,1].reshape((2, 2))
Z_R = cube[:,2].reshape((2, 2))

#ax.plot_surface(X_R,Y_R,-Z_R, color="red", alpha=0.5)
#ax.plot_surface(X_R,Y_R,Z_R, color="red", alpha=0.5)
ax.plot_surface(X_R,Z_R,Y_R, color="green", alpha=.5)
ax.plot_surface(X_R*-2,Z_R*-2,Y_R*-2, color="red", alpha=.5)
#ax.view_init(elev = 60, azim=30)
#ax.plot_surface(X_R,-Z_R,Y_R, color="red", alpha=0.5)
#ax.plot_surface(-Z_R,X_R,Y_R, color="red", alpha=0.5)
#ax.plot_surface(Z_R,X_R,Y_R, color="red", alpha=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()