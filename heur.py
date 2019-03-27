import algorithm_framework_for_SAP as d
#d.operators_selected=[0,1,2]
#d.mip_solver="cplex" or "cbc" 
d.solver_mipgap=0.00000000001
d.readfile("zys_13b.txt", "zys_connectivity.txt")
# read an instance: unit file and connectivity file
d.set_solver_params(13,"ils",10,300,1,-1)
#d.set_solver_params(13,"sa",10,300,1,-1)
#d.set_solver_params(13,"sls",10,300,1,-1)
#d.set_solver_params(13,"vns",10,300,1,-1)
#d.set_solver_params(13,"rrt",10,300,1,-1)

#solver parameters:
#13 - number of facilities
#"ils" - algorithm such as ils, ilsvnd, vns, sa, sls, rrt 
#10 - number of initial solutions
#300 - heuristic time in seconds
#1 - spp modeling
#-1 - random seed

d.solve() #solve the instance
d.print_solution()
