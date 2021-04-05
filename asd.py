
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

face = np.array([[-2, -2, -2], [2, -2, -2], [-2, -2, 2], [2, -2, 2]])

#x = face[:,0].reshape((2, 2))
"""
face[0,:] = face[0,:]*R
face[1,:] = face[1,:]*R
face[2,:] = face[2,:]*R
face[3,:] = face[3,:]*R
"""
#print(face[1,:])
face = face*R
#print(face)

X_R = face[:,0].reshape((2, 2))
Y_R = face[:,1].reshape((2, 2))
Z_R = face[:,2].reshape((2, 2))

face2 = face[[2,3],:]
face2 = np.vstack((face2, face2*.5))
X_R2 = face2[:,0].reshape((2, 2))
Y_R2 = face2[:,1].reshape((2, 2))
Z_R2 = face2[:,2].reshape((2, 2))

face3 = face[[0,2],:]
face3 = np.vstack((face3, face3*.5))
X_R3 = face3[:,0].reshape((2, 2))
Y_R3 = face3[:,1].reshape((2, 2))
Z_R3 = face3[:,2].reshape((2, 2))

face4 = face[[0,1],:]
face4 = np.vstack((face4, face4*.5))
X_R4 = face4[:,0].reshape((2, 2))
Y_R4 = face4[:,1].reshape((2, 2))
Z_R4 = face4[:,2].reshape((2, 2))

face5 = face[[1,3],:]
face5 = np.vstack((face5, face5*.5))
X_R5 = face5[:,0].reshape((2, 2))
Y_R5 = face5[:,1].reshape((2, 2))
Z_R5 = face5[:,2].reshape((2, 2))

#ax.plot_surface(X_R,Y_R,-Z_R, color="red", alpha=0.5)
#ax.plot_surface(X_R,Y_R,Z_R, color="red", alpha=0.5)
ax.plot_surface(X_R*.5,Y_R*.5,Z_R*.5, color="green", alpha=.7)
ax.plot_surface(X_R,Y_R,Z_R, color="red", alpha=.5)
ax.plot_surface(X_R2,Y_R2,Z_R2, color="red", alpha=.5)
ax.plot_surface(X_R3,Y_R3,Z_R3, color="red", alpha=.5)
ax.plot_surface(X_R4,Y_R4,Z_R4, color="red", alpha=.5)
ax.plot_surface(X_R5,Y_R5,Z_R5, color="red", alpha=.5)
ax.view_init(elev = 20, azim=130)
ax.set_ylim(-2.5,2.5)
ax.set_xlim(-2.5,2.5)
ax.set_zlim(-2.5,2.5)
#ax.plot_surface(X_R,-Z_R,Y_R, color="red", alpha=0.5)
#ax.plot_surface(-Z_R,X_R,Y_R, color="red", alpha=0.5)
#ax.plot_surface(Z_R,X_R,Y_R, color="red", alpha=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()