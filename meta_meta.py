import time

def timethis(func):
	'''
	Decorator that reports the execution timethis
	'''
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
