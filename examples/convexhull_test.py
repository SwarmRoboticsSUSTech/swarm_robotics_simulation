'''
Reference: https://matplotlib.org/api/path_api.html#matplotlib.path.Path.contains_point
'''

from scipy.spatial import ConvexHull
from matplotlib.path import Path
import numpy as np
points = np.array([(1,1),(-1,-1),(1,-1),(-1,1)])
test_point = (2,0)
hull = ConvexHull( points )
hull_path = Path( points[hull.vertices] )
print (hull_path.contains_point(test_point))
