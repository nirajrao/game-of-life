class Board:

	def __init__(self, gridSize):
		self.gridSize = gridSize
		self.grid = []
		for i in range(0, gridSize):
			row = [0] * self.gridSize
			self.grid.append(row)

	def print_board(self):
		for i in range(self.gridSize):
			print(self.grid[i])

			


test_board = Board(8)
test_board.print_board()



