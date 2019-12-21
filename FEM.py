from fenics import *
import numpy as np
# Create mesh and define function space
from mshr import *

# Defining the mesh
domain = Circle(Point(0.0, 0.0), 1.0)
n = 20
mesh = generate_mesh(domain, n)

V = FunctionSpace(mesh, 'P', 1)

# Define boundary condition
# u_D = Expression('1 + x[0]*x[0] + 2*x[1]*x[1]', degree=2)
u_D = 0

def boundary(x, on_boundary):
    return on_boundary

bc = DirichletBC(V, u_D, boundary)
# Defining the load
beta = 8
R0 = 0.6
p = Expression('4*exp(-pow(beta,2)*(pow(x[0], 2) + pow(x[1]-R0, 2)))',beta=beta, R0=R0, degree=2)


# Defining the variational problem
w = TrialFunction(V)
v = TestFunction(V)
a = dot(grad(w), grad(v))*dx
L = p*v*dx

w = Function(V)
solve(a == L, w, bc)


# Plot solution
w.rename('w', 'solution')
plot(w)
plot(mesh)

# Save solution to file in VTK format
vtkfile = File('poisson.pvd')
vtkfile << w

# Plotting the solution
p = interpolate(p, V)
plot(w, title='Deflection')
plot(p, title='Load')

vtkfile_w = File('membrane_deflection.pvd')
vtkfile_w << w
vtkfile_p = File('membrane_load.pvd')
vtkfile_p << p

import matplotlib.pyplot as plt
plt.figure()
tol = 1E-8  # avoid hitting points outside the domain
y = np.linspace(-0.99+tol, 0.99-tol, 101)
points = [(0, y_) for y_ in y]  # 2D points
w_line = np.array([w(point) for point in points])
p_line = np.array([p(point) for point in points])
plt.plot(y, 100*w_line, 'r-', y, p_line, 'b--') # magnify w
plt.legend(['100 x deflection', 'load'], loc='upper left')
plt.xlabel('y'); plt.ylabel('$p$ and $100u$')
plt.savefig('plot.pdf'); plt.savefig('plot.png')

plt.show()
