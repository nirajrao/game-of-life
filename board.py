from cell import Cell
import numpy as np

class Board:

	def __init__(self, gridSize):
		self.gridSize = gridSize
		self.grid = []
		for i in range(0, gridSize):
			row = []
			for j in range(0, gridSize):
				row.append(Cell())
			self.grid.append(row)

	def print_board(self):
		for row in self.grid:
			cell_row = ""
			for cell in row:
				cell_row += cell.displaySymbol()
				cell_row += " "
			print(cell_row)

	def activateCell(self, row, col):
		currentCell = self.returnCell(row, col)
		currentCell.activate()

	def deactivateCell(self, row, col):
		currentCell = self.returnCell(row, col)
		currentCell.deactivate()

	def returnCell(self, row, col):
		return self.grid[row][col]

	def spawnRandom(self):
		for i in range(0, self.gridSize):
			row = np.random.random_integers(self.gridSize - 1)
			col = np.random.random_integers(self.gridSize - 1)
			currentCell = self.returnCell(row, col)
			currentCell.activate()







