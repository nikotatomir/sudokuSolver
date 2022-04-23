import numpy as np
import math


class board:

	def __init__(self, fileName):
		self.fileName = fileName

		self.grid = self.getGrid()
		self.gridSize = len(self.grid)
		self.boxSize = int( len(self.grid)**2 )
		self.numberOfSubgrids = int(math.sqrt(self.gridSize))
		
		self.boxValues = self.getBoxValues()


	def getGrid(self) -> np.ndarray:
		'''returns 2-D numpy array grid with intial setup of NxN sudoku puzzle'''
		grid = np.loadtxt(self.fileName, delimiter=',', skiprows=0, dtype = np.int32)
		return grid

	# initialBoxValues
	def getBoxValues(self) -> tuple:
		'''returns 1-D tuple of length N^2 with intial setup of NxN sudoku puzzle'''
		boxValues = tuple( self.grid.flatten() )
		return boxValues

	def getRowIndex(self, boxId: int) -> int:
		rowIndex = boxId // self.gridSize
		return rowIndex

	def getColumnIndex(self, boxId: int) -> int:
		columnIndex = boxId % self.gridSize
		return columnIndex

	def getSubgridIndex(self, boxId: int) -> int:
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
		i = self.numberOfSubgrids * ( subgridIndex // self.numberOfSubgrids )
		j =self.numberOfSubgrids * ( subgridIndex % self.numberOfSubgrids )
		return (i,j)

	@staticmethod
	def validBoard(currentGrid: np.ndarray) -> bool:
		pass