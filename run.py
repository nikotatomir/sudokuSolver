import numpy as np

from board import board
from backtrackingAlgorithm import backtrackingAlgorithm
from visualization import visualization

#-----------------------USER-INPUTS-----------------------#
fileName = '4x4.txt'

#-------------------------SOLVER--------------------------#
# Instanciating board class. Loading sudoku puzzle and computing all necessary properties for computation
print('Reading Sudoku Puzzle...')
board = board('9x9.txt') 

# Instanciating visualization class.
visualize = visualization(board)
print('Plotting Initial Sudoku Puzzle...')
visualize.plotUnsolvedSudoku()

# Instanciating the backtrackingAlgorithm class and computing the necessary properties for further computation.
sudoku = backtrackingAlgorithm(board)
# Running the backtracking algorithm
print('Solving...', end=' ')
sudoku.solve()
print('Finished!')

# Plotting the solved Sudoku Puzzle
visualize.plotSolvedSudoku()

# Checking if all contraints are met
print('Checking If All Game Contraints Are Met...', end=' ')
if board.validBoard():
	print('Yes, Solution Valid!')
else:
	print('No, Solution Not Valid!')
print('Done.')