import algorithm_framework_for_SAP as d
#d.operators_selected=[0]
# [0] - use one-unit-move operator 
# [0,1] - use one-unit-move and two-unit-move operators
# [0,1,2] - use three operator, default 

# d.mip_solver="cplex" # "cplex", "cbc" or ""
d.readfile("zys_13a.txt", "zys_connectivity.txt")
# read an instance: unit file and connectivity file

d.ga(13,20,300, -1, 0.7, 0.03, 1,-1)
# solve the problem by hybrid heuristic GA+LS+SPP
# 13: number of facility
# 20: population size
# 300: the time limit in second
# -1: crossover method. 0 uniform, 1 order1, 2 order2, 9 no crossover, -1 random method
# 0.7: crossover possibility of 0.3=1-0.7
# 0.03: mutation possibility
# 1: use SSP modeling? 1 yes, 0 no.
# -1: random seed

d.print_solution()
# print the final solution



