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
print(countdown.__name__)

# The following will run the original function
# only works if @wraps(func) has been used
countdown.__wrapped__(100000)

# a decorator that takes arguments
import logging

logging.basicConfig(filename="meta.log", level=logging.DEBUG)

def logged(level, message=None):
	'''
	Add logging to function
	'''
	def decorate(func):
		log = logging.getLogger(func.__module__)
		logmsg = message if message else func.__name__
		
		@wraps(func)
		def wrapper(*args, **kwargs):
			log.log(level, logmsg)
			return func(*args, **kwargs)
		return wrapper
	return decorate

# example	
@logged(logging.DEBUG)
def add(x, y):
	return x + y
	
print(add(2,3))