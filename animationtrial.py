import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LightSource
from matplotlib.animation import FuncAnimation, FFMpegWriter

ls = LightSource(azdeg=315, altdeg=45)


plt.rcParams['figure.facecolor'] = '#121212'
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor("#121212")
ax.set_axis_off()

# Define Origin
origin = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) # Start points for X, Y, Z

# 2. Define the Coordinate Axes

axis_vectors = np.array([
    [60, 0, 0],  
    [0, 60, 0], 
    [0, 0, 60]  
])


ax.plot([-50, 50], [0, 0], [0, 0], color='#3A3A3A', linewidth=2) # X-axis
ax.plot([0, 0], [-50, 50], [0, 0], color='#3A3A3A', linewidth=2) # Y-axis
ax.plot([0, 0], [0, 0], [-50, 50], color='#3A3A3A', linewidth=2) # Z-axis


ax.text(35, 0, 0, "X", color='white', fontsize=12)
ax.text(0, 35, 0, "Y", color='white', fontsize=12)
ax.text(0, 0, 35, "Z", color='white', fontsize=12)


ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.set_zlim([-20,20])

r = np.linspace(0, 30, 100)        
theta = np.linspace(0, 2*np.pi, 100) 
R, THETA = np.meshgrid(r, theta)


X = R * np.cos(THETA)
Y = R * np.sin(THETA)


Z = np.sin(R)*np.exp(-R/8)
surf = [ax.plot_surface(X, Y, Z, cmap='viridis', antialiased=True, alpha=0.8, vmin=-0.5, vmax=0.5)]


ax.set_zlim(-2, 2)
ax.set_box_aspect([1, 1, 1])

def update(frame, surf):
    
    surf[0].remove()
    
    Z_new = np.sin(R - frame / 10.0)*np.exp(-R/8) 
    
    surf[0] = ax.plot_surface(X, Y, Z_new, cmap='viridis', antialiased=True, alpha=0.8, vmin=-0.5, vmax=0.5)
    # elev = vertical angle (0 is ground level, 90 is looking straight down)
    # azim = horizontal rotation
    ax.view_init(elev=21+np.sin(frame/31.4)*21, azim=45+2*frame)
    return surf


ani = FuncAnimation(fig, update, frames=256, fargs=(surf,), interval=50, blit=False)

plt.show()

writer = FFMpegWriter(fps=24, bitrate=2000)
ani.save("Sinwave_animation.mp4", writer=writer)

print("Export Complete")