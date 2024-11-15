import numpy as np
import scipy
import matplotlib.pyplot as plt
import scipy.integrate
from manim.mobject.opengl.opengl_vectorized_mobject import OpenGLVMobject
from manim import * 


# Equations  
# Note: (A symmetric and Real) or (A hermitian and Complex) => orthogonal eigenvectors 
# x' = Ax  (A has real eigenvalues with the oppsite sign) 

# Solution
# Let v1, v2 be the eigenvectors 
# x(t) = c1 v1 e^(rt) + c2 v2 e^(st)


# Critical Point here is called the saddle point 
# Visuals 