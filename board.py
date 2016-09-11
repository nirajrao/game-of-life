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

	def returnRow(self, row):
		return self.grid[row]

	def returnSize(self):
		return self.gridSize

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

	def returnNumberOfAliveNeighbours(self, row, col):
		numCellsAlive = 0
		neighborCells = self.returnNeighbors(row, col)
		currentCell = self.returnCell(row, col)
		for cell in neighborCells:
			if (currentCell != cell):
				if (cell.alive()):
					numCellsAlive += 1
		return numCellsAlive

	def returnNeighbors(self, row, col):
		try:
			neighborCells = []
			currentCell = self.returnCell(row, col)
			for rows in range(row - 1, row + 2):
				for cols in range(col - 1, col + 2):
					if (self.returnCell(rows,cols) != currentCell):
						neighborCell = self.returnCell(rows, cols)
						neighborCells.append(neighborCell)
		except IndexError:
			pass
		finally:
			return neighborCells











