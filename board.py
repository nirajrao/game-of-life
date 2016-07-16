from cell import Cell

class Board:

	def __init__(self, gridSize):
		self.gridSize = gridSize
		self.grid = []
		for i in range(0, gridSize):
			row = [Cell().displaySymbol()] * self.gridSize
			self.grid.append(row)

	def print_board(self):
		for i in range(self.gridSize):
			print(self.grid[i])

	def activateCell(self, row, col):
		currentCell = grid[row][col]
		currentCell.activate()

	def deactivateCell(self, row, col):
		currentCell = grid[row][col]
		currentCell.deactivate()







