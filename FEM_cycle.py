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
beta = 4 # 8
R0 = 0.6

n_timesteps = 100
for beta in range(2, 20, 1):
	#beta = beta + beta/n_timesteps*20
	p.beta = beta
	#p = Expression('4*exp(-pow(beta,2)*(pow(x[0], 2) + pow(x[1]-R0, 2)))',beta=beta, R0=R0, degree=2)
	print(beta)

# Defining the variational problem
	w = TrialFunction(V)
	v = TestFunction(V)
	a = dot(grad(w), grad(v))*dx
	L = p*v*dx

	w = Function(V)
	solve(a == L, w, bc)


# Plot solution
	w.rename('w', 'solution')

# Save solution to file in VTK format
	vtkfile = File('poisson_' + str(i) + '.pvd')
	vtkfile << w

# Plotting the solution
	p = interpolate(p, V)

	vtkfile_w = File('membrane_deflection_' + str(i) + '.pvd')
	vtkfile_w << w
	vtkfile_p = File('membrane_load_' + str(i) + '.pvd')
	vtkfile_p << p


