import time
from functools import wraps

def timethis(func):
	'''
	Decorator that reports the execution timethis
	'''
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(func.__name__, end - start)
		return result
	return wrapper

@timethis
def countdown(n):
	'''
	Counts down
	'''
	while n > 0:
		n -= 1
		
countdown(100000)
# The following returns "wrapper" without @wraps(func)
# and "countdown with @wraps(func)
print(countdown.__name__) # 
