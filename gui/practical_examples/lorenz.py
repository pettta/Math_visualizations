import numpy as np
import scipy
import matplotlib.pyplot as plt
import scipy.integrate
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

    return scipy.integrate.solve_ivp(lorenz_system, t_span, initial_condition, dense_output=True).y.T


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
        self.play(Create(curve), run_time=time)
        self.interactive_embed()

