from cell import Cell
from board import Board

class Simulation:

	def __init__(self, boardSize):
		self.gameBoard = Board(boardSize)
		self.gameBoard.returnCell(4,3).activate()
		self.gameBoard.returnCell(5,4).activate()
		self.gameBoard.returnCell(5,2).activate()
		self.gameBoard.returnCell(6,3).activate()
		self.gameBoard.returnCell(6,4).activate()
		self.gameBoard.print_board()
		print("---------------")
		count = 0
		while count < 20:
			deactivateArray = []
			activateArray = []
			for i in range(0, boardSize):
				for j in range(0, boardSize):
					currentCell = self.gameBoard.returnCell(i, j)
					numNeighborsAlive = self.gameBoard.returnNumberOfAliveNeighbours(i, j)
					if (currentCell.alive()):
						if (numNeighborsAlive < 2 or numNeighborsAlive > 3):
							deactivateArray.append(currentCell)
					elif (currentCell.alive() == False):
						if (numNeighborsAlive == 3):
							activateArray.append(currentCell)
			for cell in deactivateArray:
				cell.deactivate()
			for cell in activateArray:
				cell.activate()
			count += 1
			self.gameBoard.print_board()
			print("---------------")


Simulation = Simulation(8)








		