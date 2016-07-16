from cell import Cell
from board import Board

directions [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
############   N      NE    E     SE    S     SW     W       NW

class Simulation:

	def __init__(self, boardSize):
		self.gameBoard = Board(boardSize)

	def returnNumberOfAliveNeighbours(self, row, col):
		numCellsAlive = 0
		if (row > 0):
			



		