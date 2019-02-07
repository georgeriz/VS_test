import math

try:
	math.sqrt(-1)
except ValueError:
	print('ValueError')
	
import cmath

print(cmath.sqrt(-1)) # 1j