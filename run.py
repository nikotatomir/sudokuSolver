import numpy as np

from board import board
from backtrackingAlgorithm import backtrackingAlgorithm
from visualization import visualization

board = board('9x9.txt') 
visualize = visualization(board)
visualize.plotUnsolvedSudoku()
solve = backtrackingAlgorithm(board)

for i in board.grid:
	print(i)
print()
valid = board.validBoard()
print(valid)
# print(solve.getRowIndexList())
# print(solve.getColumnIndexList())
# # print(solve.getSubgridIndexList())
# print(solve.getSubgridMatrixIndexList())

# c = solve.getCandidatesList()
# c[0].remove(5)
# for candidate in c:
# 	print(candidate)

# print(solve.validCandidate(5, 76))
solve.solve()
for i in range(5):
	print()
for i in board.grid:
	print(i)

valid = board.validBoard()
print(valid)

a = board.grid.flatten()
a[0] = 0
print(a)
print(board.grid)

visualize.plotSolvedSudoku()

# i = np.zeros(9)
# i = board.grid[:,0].copy()
# i[0] = 0
# print(type(i))
# print(i)
# print(board.grid)