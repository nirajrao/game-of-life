import unittest
from board import Board
from cell import Cell

class testBoardCreation(unittest.TestCase):

	def testBoardCreation(self):
		test_board = Board(8)
		for i in range(test_board.gridSize):
			for j in range(test_board.gridSize):
				self.assertEqual(test_board.returnCell(i, j).displaySymbol(), "X")

	def testRandomCellStateChange(self):
		test_board = Board(9)
		test_board.activateCell(3,2)
		test_board.activateCell(4,2)
		test_board.activateCell(3,5)
		test_board.activateCell(7,8)
		test_board.activateCell(1,5)
		test_board.activateCell(7,2)
		test_board.deactivateCell(3,2)
		test_board.deactivateCell(7,2)
		test_board.deactivateCell(4,2)
		self.assertEqual(test_board.returnCell(7,2).displaySymbol(),"X")
		self.assertEqual(test_board.returnCell(7,8).displaySymbol(),"O")

	def testNumAliveNeighbors(self):
		test_board = Board(8)
		test_board.returnCell(4,3).activate()
		test_board.returnCell(5,4).activate()
		test_board.returnCell(5,2).activate()
		test_board.returnCell(6,3).activate()
		test_board.returnCell(6,4).activate()
		self.assertEqual(test_board.returnNumberOfAliveNeighbours(6,3), 3)



if __name__ == "__main__":
	unittest.main()




