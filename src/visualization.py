import matplotlib.pyplot as plt

class visualization:

	# delXposition, delYposition, fontsize
	properties = {
		'4x4': {'fontsize': 28, 'singleDigits': (0.4, 0.4), 'doubleDigits': (None,None)},
		'9x9': {'fontsize': 16, 'singleDigits': (0.375, 0.375), 'doubleDigits': (None,None)},
		'16x16': {'fontsize': 10, 'singleDigits': (0.375, 0.35), 'doubleDigits': (0.25,0.35)},
		'25x25': {'fontsize': 8, 'singleDigits': (0.325, 0.325), 'doubleDigits': (0.175,0.325)}
	}

	def __init__(self, board):
		self.board = board
		self.dimension = str(self.board.gridSize)+'x'+str(self.board.gridSize)

	def canvas(self):
		'''returns the matplotlib template upon which all data is plotted'''
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
		'''plots the initial sudoku puzzle'''
		plt.figure(1,figsize=(7,7))
		self.canvas()
		# computing coordinates for plotting initial values
		boxCoordinates = []
		boxId = 0
		for yValue in reversed(range(self.board.gridSize)):
			for xValue in range(self.board.gridSize):
					if self.board.fixedBoxValues[boxId] < 10:
						deltaX, deltaY = visualization.properties[self.dimension]['singleDigits'][0], visualization.properties[self.dimension]['singleDigits'][1]
						boxCoordinates.append((xValue+deltaX, yValue+deltaY))
					elif self.board.fixedBoxValues[boxId] >= 10:
						deltaX, deltaY = visualization.properties[self.dimension]['doubleDigits'][0], visualization.properties[self.dimension]['doubleDigits'][1]
						boxCoordinates.append((xValue+deltaX, yValue+deltaY))
					else:
						pass	
					boxId += 1
		# plotting initial values
		for boxId in range(self.board.boxSize):
			fixedBoxValue = self.board.fixedBoxValues[boxId]
			if fixedBoxValue == 0:
				pass
			else:
				xCoordinate, yCoordinate = boxCoordinates[boxId][0], boxCoordinates[boxId][1]
				plt.text(xCoordinate, yCoordinate, fixedBoxValue, fontsize = visualization.properties[self.dimension]['fontsize'], color = '#000000') #, backgroundcolor = '#f4f4f4')		
		plt.title(f'{self.dimension} Sudoku (Unsolved)', fontsize = 20)
		plt.savefig(f'{self.dimension}unsolvedSudokuPuzzle.png', dpi = 250)

	def plotSolvedSudoku(self):
		'''plots the solution to the sudoku puzzle'''
		plt.figure(2,figsize=(7,7))
		self.canvas()
		flattendGrid = self.board.grid.flatten()
		# computing coordinates for plotting initial values
		boxCoordinates = []
		boxId = 0
		for yValue in reversed(range(self.board.gridSize)):
			for xValue in range(self.board.gridSize):
					if flattendGrid[boxId] < 10:
						deltaX, deltaY = visualization.properties[self.dimension]['singleDigits'][0], visualization.properties[self.dimension]['singleDigits'][1]
						boxCoordinates.append((xValue+deltaX, yValue+deltaY))
					elif flattendGrid[boxId] >= 10:
						deltaX, deltaY = visualization.properties[self.dimension]['doubleDigits'][0], visualization.properties[self.dimension]['doubleDigits'][1]
						boxCoordinates.append((xValue+deltaX, yValue+deltaY))
					else:
						pass	
					boxId += 1

		# plotting solution values
		for boxId in range(self.board.boxSize):
			xCoordinate, yCoordinate = boxCoordinates[boxId][0], boxCoordinates[boxId][1]
			fixedBoxValue = self.board.fixedBoxValues[boxId]

			if fixedBoxValue == 0:
				plt.text(xCoordinate, yCoordinate, flattendGrid[boxId], fontsize = visualization.properties[self.dimension]['fontsize'], color = 'r')
			else:
				plt.text(xCoordinate, yCoordinate, flattendGrid[boxId],fontsize = visualization.properties[self.dimension]['fontsize'], color = '#000000')		

		plt.title(f'{self.dimension} Sudoku (Solution)', fontsize = 20)
		plt.savefig(f'{self.dimension}solvedSudokuPuzzle.png', dpi = 250)
