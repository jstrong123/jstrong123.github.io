import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.animation import FuncAnimation

# Set font properties using rcParams
plt.rcParams['font.family'] = 'serif'  # Set font family
plt.rcParams['font.size'] = 12  # Set font size
#plt.rcParams['font.weight'] = 'bold'  # Set font weight

# Sample data
T = 12
time_arr = np.linspace(0, T, T)
x_path = [0, 0.1, -0.3, -0.1, -0.5, -0.2, 0.3, 0.6, 0.1, 0.2, -0.3, 0]
y_path = [0, 0.1, 0.1, 0.4, 0.6, 0.2, 0.1, -0.3, -0.1, -0.2, -0.3, 0]

# Create a color gradient based on the time index
colors = cm.magma(np.linspace(0, 1, T))

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot entire path
for i in range(T - 1):
   ax.plot(x_path[i:i + 2], y_path[i:i + 2], time_arr[i:i + 2], color=colors[i])


# Initialize scatter plot for animating point
point, = ax.plot([], [], [], 'ro')

# Initialize line plot
line, = ax.plot([], [], [], linewidth=2)

# Update function for animation
def update(frame):
    # Update line plot
    line.set_data(x_path[:frame+1], y_path[:frame+1])
    line.set_3d_properties(time_arr[:frame+1])
    # Set color of the line based on the current frame
    #line.set_color(colors[frame])

    # Update animating point
    point.set_data(x_path[frame], y_path[frame])
    point.set_3d_properties(time_arr[frame])
    
    return line, point



# Create animation
ani = FuncAnimation(fig, update, frames=T, interval=400, blit=True)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Imaginary time index')
ax.set_title('3D Path')

# Set view angle
ax.view_init(azim=45, elev=15)

plt.show()

ani.save('animation.gif', writer='imagemagick')