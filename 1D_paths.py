# PATHS

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.animation import FuncAnimation

# Set font properties using rcParams
plt.rcParams['font.family'] = 'serif'  # Set font family
plt.rcParams['font.size'] = 12  # Set font size

# Define parameters
N = 10
T = 12
eta = T / N
m = 5
omega = 0.7
hbar = 1
a_B = 1.03 * 10**-8
a = eta
x_start = -4
x_end = 4
x_range = x_end - x_start
step = 0.1
n_points = int(x_range / step) + 1

# Generate spatial points
spatial_points = np.linspace(x_start, x_end, n_points)

# Create a color gradient based on the time index
colors = cm.magma(np.linspace(0, 1, T))

time_arr = np.linspace(0, T, T)

# 1D

path = [0, 0.1, 0.3, -0.1, 0, -0.5,-0.2, 0.4, 0.1, -0.3, 0.2, 0]

# Initialize the plot
fig, ax = plt.subplots()

# Plot each segment of the path with its corresponding color
for i in range(len(path) - 1):
    ax.plot(time_arr[i:i+2], path[i:i+2], color=colors[i], marker='', label=f'Segment {i+1}')


line, = ax.plot([], [])

point, = ax.plot([], [], 'ro')

plt.axhline(y=0, color='r', linestyle='--') 
plt.xlabel(r'Imaginary Time index')
plt.ylabel(r'X')
ax.set_title('1D Path')

# Initialize function to update the plot for each frame
def update(frame):
    line.set_data(time_arr[:frame+1], path[:frame+1])
    point.set_data(time_arr[frame], path[frame])
    return line, point

# Animate the plot
ani = FuncAnimation(fig, update, frames=len(path), interval=400, blit=True)

plt.show()

ani.save('animation1D.gif', writer='imagemagick')