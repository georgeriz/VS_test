class Customer():
	def __init__(self, name, orders):
		self.name = name
		self.orders = orders
		
	def destroy(self):
		pass
		
	def __repr__(self):
		return self.name