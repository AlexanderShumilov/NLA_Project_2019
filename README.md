# NLA_Project_2019
Numerical Linear Algebra Project 2019, Team 25.

To reproduce results be sure that you have proper libraries for work with vtk-format files, because the solutions of FEM stored in such files. To get the solutions you should install FEniCS from here: https://fenicsproject.org/download/, Linux version seems the easiest one to deal with. To reproduce animations you can use ParaView.

# Content:

1) FEM.py : FEniCS script for FEM
2) FEM_cycle.py : the same as previous one, but with inner cycle for obtaining results for different membrane pressure
3) Project (2).ipynb : main file containing compression algorithm (plots, comparisons and bullet points included)
4) Project_for_cluster (2).ipynb : practically the same, but designed to be run on Zhores cluster (for computational-heavy measurements)
5) n = 20.zip : pre-processed vtk-files (FEM solutions for not very dense grid) for eliminating fenics instalation during data testing
6) /Presentation : files for project presentations, animations included
