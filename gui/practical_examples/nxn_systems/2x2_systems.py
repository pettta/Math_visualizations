import numpy as np
import scipy
import matplotlib.pyplot as plt
import scipy.integrate
from manim.mobject.opengl.opengl_vectorized_mobject import OpenGLVMobject
from manim import * 

"""
This file contains the following examples of 2x2 systems of ODEs that solve:
Ax = x' where A is a square matrix, x is a vector, and x' is the vector containing the derivatives of x. 
TODO parent class that contains the common methods and attributes of 2x2 systems, etc... 
TODO graphing speedups 
TODO gui for user to input matrix live and re-render the scene
"""
def find_eigenpairs(matrix):
    """
    Finds the eigenvectors of a matrix 
    """
    eigvals, eigvecs = np.linalg.eig(matrix)
    # if the matrix is symmetric, the eigenvectors are orthogonal 
    # else get generalized eigenvectors
    # TODO 
    return eigvals, eigvecs 

    

#======= Real EigenValues with Same Sign ========#
### Equations: x(t) =  c1*xi_1*e^(r1t) + c2*xi_2*e^(r2t) 
### CASE 1: r1 > r2 > 0 (positive real eigenvalues)
# Critical Point here is called the node : unstable node 
class RealEigenValuesPositiveSameSign(Scene):
    def construct(self):
        time=5
        time_span = [0, time] 
        A = np.array([[1, 1], [0, 1]])
        points_container = []
        for i in range(4): #four quadrants
            for j in range(5): # five points in each quadrant
                x_sign = 1 if i % 2 == 0 else -1
                y_sign = 1 if i < 2 else -1
                ic = [5.0 * x_sign * (j + 1), 5.0 * y_sign * (j + 1)]
                points = scipy.integrate.solve_ivp(lambda t, x: A @ x, time_span, ic, dense_output=True).y.T
                points_container.append(points)

        axes=Axes(x_range=[-1000,1000], y_range=[-1000,1000])
        axes.set_width(200)
        axes.center()
        self.add(axes)
        colors = {0: RED, 1: BLUE, 2: GREEN, 3: YELLOW}
        for loc, points in enumerate(points_container):
            curve = OpenGLVMobject().set_points_as_corners(axes.c2p(points))
            curve.set_stroke(colors[loc%4], 2)
            self.play(Create(curve), run_time=1)
        self.interactive_embed()

### CASE 2: r1 < r2 < 0 (negative real eigenvalues)
# Critical Point here is called the node: asymptotically stable node 
class RealEigenValuesNegativeSameSign(Scene):
    def construct(self):
        time=5
        time_span = [0, time] 
        A = np.array([[-1, 1], [0, -1]])
        points_container = []
        for i in range(4): #four quadrants
            for j in range(5): # five points in each quadrant
                x_sign = 1 if i % 2 == 0 else -1
                y_sign = 1 if i < 2 else -1
                ic = [5.0 * x_sign * (j + 1), 5.0 * y_sign * (j + 1)]
                points = scipy.integrate.solve_ivp(lambda t, x: A @ x, time_span, ic, dense_output=True).y.T
                points_container.append(points)

        axes=Axes(x_range=[-100,100], y_range=[-100,100])
        axes.set_width(20)
        axes.center()
        self.add(axes)
        colors = {0: RED, 1: BLUE, 2: GREEN, 3: YELLOW}
        for loc, points in enumerate(points_container):
            curve = OpenGLVMobject().set_points_as_corners(axes.c2p(points))
            curve.set_stroke(colors[loc%4], 2)
            self.play(Create(curve), run_time=1)
        self.interactive_embed()

#======= Real EigenValues with Opposite Sign ========#
### Equations: x(t) = c1 xi_1 e^(rt) + c2 xi_2 e^(st)
# A symmetric and Real or A hermitian and Complex => orthogonal eigenvectors
# Critical Point here is called the Saddle Pt: unstable 
class RealEigenValuesOppositeSign(Scene):
    def construct(self):
        time=5
        time_span = [0, time] 
        A = np.array([[3, -2], [2, -2]])
        points_container = []
        for i in range(4): #four quadrants
            for j in range(5): # five points in each quadrant
                x_sign = 1 if i % 2 == 0 else -1
                y_sign = 1 if i < 2 else -1
                ic = [5.0 * x_sign * (j + 1), 5.0 * y_sign * (j + 1)]
                points = scipy.integrate.solve_ivp(lambda t, x: A @ x, time_span, ic, dense_output=True).y.T
                points_container.append(points)

        axes=Axes(x_range=[-100,100], y_range=[-100,100])
        axes.set_width(20)
        axes.center()
        self.add(axes)
        colors = {0: RED, 1: BLUE, 2: GREEN, 3: YELLOW}
        for loc, points in enumerate(points_container):
            curve = OpenGLVMobject().set_points_as_corners(axes.c2p(points))
            curve.set_stroke(colors[loc%4], 2)
            self.play(Create(curve), run_time=1)
        self.interactive_embed()


### Visuals

#======= Equal EigenValues ========#
# Note: you can have either positive or negative equal eigenvalues, but that isn't what deliniates cases 
### CASE 1: 2 linearly independent eigenvectors from the same eigenvalue
# Equations: x(t) = c1*xi_1*e^(rt) + c2*xi_2*e^(rt)

# Critical Point here is called the proper node 
# Proper Node: asymptotically stable or unstable depending on the sign of the eigenvalues


### CASE 2: 1 linearly independent eigenvector ==> jordan block 
# Equations: x(t) = c1*xi*e^(rt) + c2 (xi*t*e^(rt) + nu*e^(rt))

# Critical Point here is called the improper or degenerate node (since A is a degenerate matrix)
# Improper Node: asymptotically stable or unstable depending on the sign of the eigenvalues

#======= Complex EigenValues with Nonzero Real Part ========#

# Equations 
# Note that antisymmetric A => complex eigenvalues with nonzero real part (not bidirectional)
# x' = Ax  (A has complex eigenvalues with some nonzero real part)
# for each eigenvalue lambda +- u*i 
#  u(t) = e^(lambda)t (a cos(ut) - b sin(ut)) 
#  v(t) = e^(lambda)t (a sin(ut) + b sin(ut)) 


# Critical Point here is called the spiral point (and it is either a source (lambda >0) or a sink(lambda <0)): unstable 
# Visuals 

#======= Complex EigenValues with Zero Real Part ========#

# Equations 
# x' = Ax  (A has complex eigenvalues with zero real part)  

# Critical Point here is called the center (orbitals) : stable 
# Visuals 


