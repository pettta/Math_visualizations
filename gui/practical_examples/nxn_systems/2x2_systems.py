import numpy as np
import scipy
import matplotlib.pyplot as plt
import scipy.integrate
from manim.mobject.opengl.opengl_vectorized_mobject import OpenGLVMobject
from manim import * 

"""
This file contains the following examples of 2x2 systems of ODEs that solve:
Ax = x' where A is a square matrix, x is a vector, and x' is the vector containing the derivatives of x. 
"""


#======= Real EigenValues with Same Sign ========#
### Equations: x(t) =  c1*xi_1*e^(r1t) + c2*xi_2*e^(r2t) 
### CASE 1: r1 > r2 > 0 (positive real eigenvalues)
# Critical Point here is called the node : unstable node 


### CASE 2: r1 < r2 < 0 (negative real eigenvalues)
# Critical Point here is called the node: asymptotically stable node 


### Visuals

#======= Real EigenValues with Opposite Sign ========#
### Equations: x(t) = c1 xi_1 e^(rt) + c2 xi_2 e^(st)
# A symmetric and Real or A hermitian and Complex => orthogonal eigenvectors
# Critical Point here is called the Saddle Pt: unstable 



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


