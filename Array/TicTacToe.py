from nose.tools import assert_equal

def tictactoe(board):

	for i in range(3):
		rowX = rowO = 0
		for j in range(3):
			if board[i][j] == 'X':
				rowX += 1
			else:
				rowO += 1
		if rowX == 3:
			return 'X wins'
		elif rowO == 3:
			return 'O wins'

	for j in range(3):
		colX = ColO = 0
		for i in range(3):
			if board[i][j] == 'X':
				colX += 1
			else:
				ColO += 1
		if colX == 3:
			return 'X wins'
		elif ColO == 3:
			return 'O wins'

	crossX = crossO = 0
	for i in range(3):
		if board[i][i] == 'X':
			crossX += 1
		else:
			crossO += 1
	if crossO == 3:
		return 'O wins'
	else:
		return 'X wins'

	crossX = crossO = 0
	j = 2
	for i in range(3):
		if board[i][j] == 'X':
			crossX += 1
		else:
			crossO == 'O'
		j -= 1
	if crossO == 3:
		return 'O wins'
	else:
		return 'X wins'

class TicTacToe_Test:
	def test(self, func):
		assert_equal(func(['XOO', 'XOO', 'OOX']), 'O wins')
		assert_equal(func(['XXX', 'OXO', 'OOX']), 'X wins')
		assert_equal(func(['XOO', 'XOX', 'XOO']), 'X wins')
		assert_equal(func(['OXX', 'XOO', 'OXO']), 'O wins')
		print('TESTS PASSED')

t = TicTacToe_Test()
t.test(tictactoe)