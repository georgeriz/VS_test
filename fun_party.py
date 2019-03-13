from functools import partial

def spam(a, b, c, d):
	print(a, b, c, d)
	
s1 = partial(spam, 1) # a = 1
s1(2, 3, 4) # 1 2 3 4

s2 = partial(spam, 1, d=42) # a = 1, d = 42
s2(3, 4) # 1 3 4 42