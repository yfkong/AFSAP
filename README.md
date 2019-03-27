# HFSAP
An heuristic framework for the service area problem (SAP)
# Problem definition and formulation
The design of service areas is one of the essential issues in providing efficient services in both the public and private sectors. For a geographic area with basic areal units, the SAP should assign the service-demand areal units to service-supply units such that each facility has a service area and some criteria are satisfied. The basic criteria for the problem include the balance of service demand and supply, the highest service accessibility, the contiguity of service areas, and the integrity of basic units. The balance criterion means that the total service demand in each area should be no greater than its service capacity. Service accessibility can be evaluated by total travel distance from demand units to their supply units. The shortest travel distance is usually preferred when using the service. Contiguous service area is also a necessity for satisfying policy or management purposes. In service area design practice, splitting a demand unit is usually not allowed.
# The metaheuristic framework
The SAP could be solved by exact methods, local-search-based metaheuristics, population-based metaheuristics or hybrid methods.
The metaheuristic framework was designed to implemented various algorithms for the SAP.
# Settings
1. Python recommended: Python 2.7.x on Windows, and pypy2 (a fast and compliant Python, http://pypy.org).
2. PuLP 1.6.0 (https://pypi.org/project/PuLP/)
3. ILOG CPLEX 12.x, cplex (CPLEX Python API)
4. Copy all the files in a directory.
5. Run the python files in a command window, such as:
* mip.py (solve the problem by exact method)
* \pypy2\pypy hybrid.py (solve the problem by the hybrid method)
* \pypy2\pypy heur.py (solve the problem by local search method)
6. The Python files can be edited.
# E-mail: yfkong@henu.edu.cn
# Read the file Introduction for detail.