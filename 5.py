import math
list=[56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
new=[x for x in list if not math.isnan(x)]
print(new)
