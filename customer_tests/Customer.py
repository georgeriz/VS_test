class Customer():
	def __init__(self, name, orders):
		self.name = name
		self.orders = orders
		
	def __str__(self):
		return self.name