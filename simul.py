from cell import Cell
from board import Board

directions [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
############   N      NE    E     SE    S     SW     W       NW

class Simulation:

	def __init__(self, boardSize):
		self.gameBoard = Board(boardSize)
		####

	def checkNeighbours(self):
		for rows in self.gameBoard:
			for cell in rows:
				if cell.isAlive()
