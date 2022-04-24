import numpy as np

from board import board
from backtrackingAlgorithm import backtrackingAlgorithm
from visualization import visualization

board = board('4x4.txt') 
visualize = visualization(board)
visualize.plotUnsolvedSudoku()
sudoku = backtrackingAlgorithm(board)
print('Solving...')
sudoku.solve()
print('Finished!')
visualize.plotSolvedSudoku()
if board.validBoard():
	print('Solution Valid!')
else:
	print('Solution Not Valid!')
