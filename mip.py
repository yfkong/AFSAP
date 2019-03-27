import algorithm_framework_for_SAP as d
d.solver_mipgap=0.00000000001
# mipgap for CPLEX
# it is recommended to use CPLEX solver 
d.readfile("zys_13b.txt", "zys_connectivity.txt")
# read an instance: unit file and connectivity file

d.mipmodel()
# create a MILP file, and sovle it by CPLEX

d.print_solution()
