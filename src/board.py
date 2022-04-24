import numpy as np
import math


class board:

	def __init__(self, fileName):
		self.fileName = fileName

		self.grid = self.getGrid()
		self.gridSize = len(self.grid)
		self.boxSize = int( len(self.grid)**2 )
		self.numberOfSubgrids = int(math.sqrt(self.gridSize))
		
		self.fixedBoxValues = self.getFixedBoxValues()


	def getGrid(self) -> np.ndarray:
		'''returns 2-D numpy array grid with intial setup of NxN sudoku puzzle'''
		grid = np.loadtxt(self.fileName, delimiter=',', skiprows=0, dtype = np.int32)
		return grid

	# initialBoxValues
	def getFixedBoxValues(self) -> tuple:
		'''returns 1-D tuple of length N^2 with intial setup of NxN sudoku puzzle'''
		fixedBoxValues = tuple( self.grid.flatten() )
		return fixedBoxValues

	def getRowIndex(self, boxId: int) -> int:
		'''returns the row index of a specific box'''
		rowIndex = boxId // self.gridSize
		return rowIndex

	def getColumnIndex(self, boxId: int) -> int:
		'''returns the column index of a specific box'''
		columnIndex = boxId % self.gridSize
		return columnIndex

	def getSubgridIndex(self, boxId: int) -> int:
		'''returns the subgrid index of a specific box'''
		subgridNumbering = np.zeros((self.numberOfSubgrids, self.numberOfSubgrids), dtype = np.int32)
		currentSubgridNumber = 0
		for i in range(self.numberOfSubgrids):
			for j in range(self.numberOfSubgrids):
				subgridNumbering[i,j] = currentSubgridNumber
				currentSubgridNumber += 1
		
		rowIndex, columnIndex = self.getRowIndex(boxId), self.getColumnIndex(boxId)
		subgridIndex = subgridNumbering[rowIndex // self.numberOfSubgrids, columnIndex // self.numberOfSubgrids]

		return subgridIndex

	def getSubgridMatrixIndex(self, subgridIndex: int) -> tuple:
		'''returns the subgrid matrix start indecies a specific subgrid'''
		i = self.numberOfSubgrids * ( subgridIndex // self.numberOfSubgrids )
		j =self.numberOfSubgrids * ( subgridIndex % self.numberOfSubgrids )
		return (i,j)

	@staticmethod
	def checkArray(array: np.ndarray) -> bool:
		'''çhecks if array(row, column, subgrid) has duplicate numbers'''
		array = array[array != 0]
		if len(array) == len(set(array)):
			return True
		else:
			return False

	def validBoard(self) -> bool:
		'''checks board validity'''
		checkRow = np.zeros(self.gridSize, dtype = np.bool)
		checkColumn = np.zeros(self.gridSize, dtype = np.bool)
		checkSubgrid = np.zeros(self.gridSize, dtype = np.bool)

		for i in range(self.gridSize):
			# check rows
			rowArray = self.grid[i,:].copy().flatten()
			checkRow[i] = board.checkArray(rowArray)
			# checkColumns
			columnArray = self.grid[i,:].copy().flatten()
			checkColumn[i] = board.checkArray(columnArray)
			# check Subgrids
			index1, index2 = self.getSubgridMatrixIndex(i)
			subgridArray = self.grid[ index1 : index1+self.numberOfSubgrids , index2 : index2+self.numberOfSubgrids ].copy().flatten()
			checkSubgrid[i] = board.checkArray(subgridArray)
			
		if np.all(checkRow) and np.all(checkColumn) and np.all(checkSubgrid):
			return True
		else:
			return False

