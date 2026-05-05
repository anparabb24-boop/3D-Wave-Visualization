# 3D Oscillating Charge Field Visualization 

A high-fidelity 3D mathematical animation built with Python, inspired by the 3Blue1Brown aesthetic. This project visualizes a decaying wave function, simulating the behavior of an electric field from an oscillating point source.

##  The Physics & Math
While the decay is exaggerated for visual clarity, this simulation models the field behavior observed when a charge oscillates about the $z$-axis. 

The surface is generated using a sinusoidal wave function coupled with an exponential decay factor:

$$Z = \sin(R - \frac{t}{10}) \cdot e^{-\frac{R}{8}}$$

Where:
*   $R = \sqrt{X^2 + Y^2}$ (Cylindrical radius)
*   $t$ = Frame offset (Time)
*   $e^{-\frac{R}{8}}$ = Spatial damping (Exponential decay)

##  What the Code Does
*   **Coordinate Transformation:** Maps a cylindrical grid (radius and theta) to Cartesian $(X, Y)$ coordinates for 3D plotting.
*   **Dynamic Rendering:** Uses `matplotlib.animation.FuncAnimation` to update the surface $Z$-values in real-time.
*   **Cinematic Camera:** The camera's perspective (`view_init`) is scripted to oscillate its elevation and rotate its azimuth, providing a full 360-degree view of the field peaks and valleys.
*   **Aesthetic Styling:** Implements a "dark mode" theme with the `viridis` colormap and controlled alpha transparency.

##  Setup & Usage

### Prerequisites
Ensure you have **FFmpeg** installed on your system to export the video:
```bash
brew install ffmpeg
