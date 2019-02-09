import math

try:
	math.sqrt(-1)
except ValueError:
	print('ValueError')
	
import cmath

print(cmath.sqrt(-1)) # 1j

a = float('nan')
print(math.isnan(a)) # the only way to test for nan

b = float('inf')
print(b/b) # nan