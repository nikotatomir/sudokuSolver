from src.board import board
from src.visualization import visualization
from src.backtrackingAlgorithm import backtrackingAlgorithm

#-----------------------USER-INPUTS-----------------------#
fileName = 'sudokuPuzzles/16x16.txt'

#-------------------------SOLVER--------------------------#
# Instanciating board class. Loading sudoku puzzle and computing all necessary properties for computation
print('Reading Sudoku Puzzle...')
board = board(fileName) 

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