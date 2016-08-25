from cell import Cell
from board import Board

class Simulation:

	def __init__(self, boardSize):
		self.gameBoard = Board(boardSize)
		self.gameBoard.spawnRandom()
		print("---------------")
		count = 0
		while count < 20:
			for i in range(0, boardSize):
				for j in range(0, boardSize):
					currentCell = self.gameBoard.returnCell(i, j)
					numNeighborsAlive = self.gameBoard.returnNumberOfAliveNeighbours(i, j)
					if (currentCell.alive()):
						if (numNeighborsAlive < 2 or numNeighborsAlive > 3):
							currentCell.deactivate()
					elif (numNeighborsAlive == 3 and currentCell.alive() == False):
						currentCell.activate()
			count += 1
			self.gameBoard.print_board()
			print("---------------")


Simulation = Simulation(8)








		