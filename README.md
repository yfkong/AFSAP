# HASAP
An algorithm framework for the service area problem (SAP)
Various algorithms can be implemented based on the framework:
1. Local-search based metaheuristics such as ILS, VNS, SA, RRT, SLS, VND, HC;
2. Population based metaheuristics such as GA, EA;
3. MILP modeling;
4. Hybrid algorithms such as GA+LS+SPP, ILS+SPP, ILS+VND, VNS+SPP...
# Read the file "Introduction_v01.pdf" for details.
# Problem definition
The design of service areas is one of the essential issues in providing efficient services in both the public and private sectors. For a geographic area with basic areal units, the SAP should assign the service-demand areal units to service-supply units such that each facility has a service area and some criteria are satisfied. The basic criteria for the problem include the balance of service demand and supply, the highest service accessibility, the contiguity of service areas, and the integrity of basic units. The balance criterion means that the total service demand in each area should be no greater than its service capacity. Service accessibility can be evaluated by total travel distance from demand units to their supply units. The shortest travel distance is usually preferred when using the service. Contiguous service area is also a necessity for satisfying policy or management purposes. In service area design practice, splitting a demand unit is usually not allowed.
# How to use the framework
1. Install the sofywares: 
* Python recommended: Python 2.7.x on Windows, and pypy2 (a fast and compliant Python, http://pypy.org);
* PuLP 1.6.0 (https://pypi.org/project/PuLP/);
* ILOG CPLEX 12.x and CPLEX Python API.
2. Copy all the files in a file directory.
3. Run the example files in a command window, such as:
* mip.py (solve the problem by exact method);
* \pypy2\pypy hybrid.py (solve the problem by the hybrid method: GA+LS+SPP);
* \pypy2\pypy heur.py (solve the problem by a population-based or multistary local-search metaheuristic, such as ILS, ILS-VND, VNS, SA, RRT, VND, SLS, HC).
# E-mail: yfkong@henu.edu.cn
