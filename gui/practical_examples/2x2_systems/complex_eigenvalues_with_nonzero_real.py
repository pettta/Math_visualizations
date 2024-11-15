import numpy as np
import scipy
import matplotlib.pyplot as plt
import scipy.integrate
from manim.mobject.opengl.opengl_vectorized_mobject import OpenGLVMobject
from manim import * 


# Equations 
# Note that antisymmetric A => complex eigenvalues with nonzero real part (not bidirectional)
# x' = Ax  (A has complex eigenvalues with some nonzero real part)
# for each eigenvalue lambda +- u*i 
#  u(t) = e^(lambda)t (a cos(ut) - b sin(ut)) 
#  v(t) = e^(lambda)t (a sin(ut) + b sin(ut)) 



# Critical Point here is called the spiral point (and it is either a source or a sink)
# Visuals 