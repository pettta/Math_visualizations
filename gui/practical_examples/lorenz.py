import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from manim.mobject.opengl.opengl_vectorized_mobject import OpenGLVMobject
from manim import * 

# Equations 
# dx/dt = sigma * (y - x) 
# dy/dt = x * (rho - z) - y
# dz/dt = x * y - beta * z 
# rho, sgima, beta are arbitrary 

def lorenz_solver(initial_condition, t_span, sigma=10, rho=28, beta=8/3):
    def lorenz_system(t, state):
        x, y, z = state
        dx_dt = sigma * (y - x)
        dy_dt = x * (rho - z) - y
        dz_dt = x * y - beta * z
        return [dx_dt, dy_dt, dz_dt]

    return solve_ivp(lorenz_system, t_span, initial_condition, dense_output=True).y.T


class OpenGLShow(Scene):
    def construct(self):
        ### Render the relevant data points 
        time = 50 
        ic = [5.0, 5.0, 5.0] 
        t_span = [0, time]
        points = lorenz_solver(ic, t_span)

        ### Render the visuals 
        axes=ThreeDAxes(x_range=[-50,50, 5], y_range=[-50,50, 5], z_range=[-0, 50, 5]) 
        axes.set_width(10)
        axes.center() 
        self.add(axes) 
        curve = OpenGLVMobject().set_points_as_corners(axes.c2p(points))
        curve.set_stroke(YELLOW, 2)
        self.play(Create(curve), run_time=50, rate_func=linear)
        self.interactive_embed()



# Example usage
# initial_condition = [1.0, 1.0, 1.0]  # Initial values for x, y, z
# time_span = [0, 100]  # Time range from 0 to 100
# t, x, y, z = lorenz_solver(initial_condition, time_span)

# # Plotting the results
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(x, y, z)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('Lorenz Attractor')
# plt.show()