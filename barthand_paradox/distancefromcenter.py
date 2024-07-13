import matplotlib.pyplot as plt
import numpy as np

def distance_from_center(r, theta, radius, center, ax):
    a=r*np.cos(theta)
    b=r*np.sin(theta)
    circle = plt.Circle(center, radius, edgecolor='black', facecolor='none') #plot the circle
    ax.add_patch(circle)
    ax.plot(*center, 'ro', label='Center (0, 0)') #plot the center
    ax.plot(a, b, 'go', label='Midpoint ({}, {})'.format(a, b), markersize=1) #plot the midpoint
    q = np.sqrt(1 - r ** 2)
    x1 =  r * np.cos(theta) + q * np.sin(theta)
    y1 =  r * np.sin(theta) - q * np.cos(theta)
    x2 =  r * np.cos(theta) - q * np.sin(theta)
    y2 =  r * np.sin(theta) + q * np.cos(theta)

    ax.plot((x1, x2), (y1, y2), color='gray', label='Chord', linewidth=0.1)

n=1000
r_rand=np.zeros(n)
theta_rand=np.zeros(n)
count=0
for i in range(n):
    r_rand[i]=np.random.uniform(0, 1)
    p=np.sqrt(1-r_rand[i]**2)
    theta_rand[i]=np.random.uniform(0, 2*np.pi)
    if (r_rand[i])<1/2:
        count+=1

radius = 1 #circle radius and center
center = (0, 0)
fig, ax = plt.subplots()
plt.grid(True)
ax.set_aspect('equal', 'box')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_title('Using Distance from center')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

for i in range(n):
    distance_from_center(r_rand[i], theta_rand[i], radius, center, ax)
print(count/(n-1))
plt.show()


