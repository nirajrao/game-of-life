import unittest
from board import Board
from cell import Cell

class testBoardCreation(unittest.TestCase):

	def testBoard(self):
		test_board = Board(8)
		test_board.activateCell(7, 7)
		self.assertEqual(test_board.returnCell(7, 7).displaySymbol(), "O")

if __name__ == "__main__":
	unittest.main()




