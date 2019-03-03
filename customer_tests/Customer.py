class Customer():
	def __init__(self, name, orders):
		self.name = name
		self.orders = orders
		
	def __repr__(self):
		return self.name