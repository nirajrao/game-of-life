class Cell:

	def __init__(self):
		self.isAlive = False
		self.symbol = "X"

	def displaySymbol(self):
		return self.symbol

	def activate(self):
		self.isAlive = True
		self.symbol = "O"

	def deactivate(self):
		self.isAlive = False
		self.symbol = "X"



