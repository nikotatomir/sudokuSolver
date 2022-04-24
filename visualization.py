import sys
import numpy as np
import matplotlib.pyplot as plt

class visualization:

	def __init__(self, board):
		self.board = board

		self.boxCoordinates = self.getBoxCoordinates()


	def getBoxCoordinates(self) -> tuple:
		'''returns a 2-D tuple of length N^2 with x,y coordinates for each of the N^2 sudoku local boxes (used for visualization)'''
		boxCoordinates = []
		for yValue in reversed(range(self.board.gridSize)):
			for xValue in range(self.board.gridSize):
				boxCoordinates.append((xValue+0.4, yValue+0.4))
		boxCoordinates = tuple(boxCoordinates)
		return boxCoordinates

	def canvas(self):
		ax = plt.axes()
		plt.xlim([0,self.board.gridSize])
		plt.ylim([0,self.board.gridSize])
		plt.tick_params(labelleft = False, left = False, labelbottom = False, bottom = False)
		ax.set_facecolor('#f8f8f8')
		
		for value in range(self.board.gridSize+1):
			modulus = value % self.board.numberOfSubgrids
			# print(modulus) 
			if modulus == 0:
				plt.axhline(y = value, linewidth = '2', color	 = 'k')
				plt.axvline(x = value, linewidth = '2', color	 = 'k')
			else:
				plt.axhline(y = value, linewidth = '0.5', color	 = 'k')
				plt.axvline(x = value, linewidth = '0.5', color	 = 'k')

	def plotUnsolvedSudoku(self):
		plt.figure(1,figsize=(7,7))
		self.canvas()
		for boxId in range(self.board.boxSize):
			fixedBoxValue = self.board.fixedBoxValues[boxId]
			if fixedBoxValue == 0:
				pass
			else:
				xCoordinate, yCoordinate = self.boxCoordinates[boxId][0], self.boxCoordinates[boxId][1]
				plt.text(xCoordinate, yCoordinate, fixedBoxValue, fontsize = 14, color = '#000000') #, backgroundcolor = '#f4f4f4')		
		plt.title('Sudoku (Unsolved)', fontsize = 20)
		plt.savefig('unsolvedSudokuPuzzle.png', dpi = 250)

	def plotSolvedSudoku(self):
		plt.figure(2,figsize=(7,7))
		self.canvas()

		flattendGrid = self.board.grid.flatten()
		for boxId in range(self.board.boxSize):
			xCoordinate, yCoordinate = self.boxCoordinates[boxId][0], self.boxCoordinates[boxId][1]
			fixedBoxValue = self.board.fixedBoxValues[boxId]

			if fixedBoxValue == 0:
				plt.text(xCoordinate, yCoordinate, flattendGrid[boxId], fontsize = 14, color = '#20aa76') #, backgroundcolor = '#f4f4f4')		
			else:
				plt.text(xCoordinate, yCoordinate, flattendGrid[boxId], fontsize = 14, color = '#000000') #, backgroundcolor = '#f4f4f4')		

		plt.title('Sudoku (Solved)', fontsize = 20)
		plt.savefig('solvedSudokuPuzzle.png', dpi = 250)
#c9f0dd
#0c4b33
#20AA76