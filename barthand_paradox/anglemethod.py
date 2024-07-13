import matplotlib.pyplot as plt
import numpy as np

def angle_method(theta, radius, center, ax):
    circle = plt.Circle(center, radius, edgecolor='black', facecolor='none') #plot the circle
    ax.add_patch(circle)
    ax.plot(*center, 'ro', label='Center (0, 0)') #plot the center
    x1=-1
    y1=0
    x2=np.cos(theta)**2-np.sin(theta)**2
    y2=(x2+1)*np.tan(theta)
    # ax.plot(*(x2, y2), 'go',markersize=1)
    ax.plot((x1, x2), (y1, y2), color='gray', label='Chord', linewidth=0.1)

n=1000
count=0
theta=np.zeros(n)
for i in range(n):
    theta[i]=np.random.rand()*np.pi
    if (theta[i]<np.pi/6 or theta[i]>5*np.pi/6):
        count+=1

radius = 1 #circle radius and center
center=(0 , 0)
fig, ax = plt.subplots()
plt.grid(True)
ax.set_aspect('equal', 'box')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_title('Using Angle Method')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.plot(*(-1, 0), 'go',markersize=1 )
for i in range(n):
    angle_method(theta[i], radius, center, ax)
print(count/n)
plt.show()