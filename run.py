

from board import board
from backtrackingAlgorithm import backtrackingAlgorithm

board = board('9x9.txt') 
solve = backtrackingAlgorithm(board)

for i in board.grid:
	print(i)

print(solve.getRowIndexList())
print(solve.getColumnIndexList())
print(solve.getSubgridIndexList())
print(solve.getSubgridMatrixIndexList())
