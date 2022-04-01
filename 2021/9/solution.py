import pdb
from classes import HeightMap
import numpy as np

f = open("9/input.txt", "r")
lines = f.read().split("\n")
#print(lines)

m = HeightMap(data=lines)
#print(m.display())
#pdb.set_trace()
low_points = m.get_low_points()
#print([p.height for p in low_points])
#print(f"Risk level is {m.get_risk_level()}")

low_point = low_points[3]
print()
basins = [m.get_basin_points(low_point=lp) for lp in low_points] 
basin_sizes = [len(b) for b in basins] 
#basins_np = np.array(basin_sizes)
#highest_three = (-basins_np).argsort()[:3]
#pdb.set_trace()
highest_three = sorted(basin_sizes, reverse=True)[:3]
#print(f"Basin for point {low_point.display()} contains {len(basin)} points.")
#print(f"These are: {[p.display() for p in basin]}")
print(f"Basins are of sizes {[b for b in highest_three]}")
print(f"Multiplied together, this yields {highest_three[0]*highest_three[1]*highest_three[2]}")
