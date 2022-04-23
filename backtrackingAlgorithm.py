

class backtrackingAlgorithm:

	def __init__(self, board):
		self.board = board

	def getRowIndexList(self) -> tuple:
		rowIndexList = []
		for boxId in range(self.board.boxSize):
			rowIndexList.append(self.board.getRowIndex(boxId))
		rowIndexList = tuple(rowIndexList)
		return rowIndexList

	def getColumnIndexList(self) -> tuple:
		columnIndexList = []
		for boxId in range(self.board.boxSize):
			columnIndexList.append(self.board.getColumnIndex(boxId))
		columnIndexList = tuple(columnIndexList)
		return columnIndexList

	def getSubgridIndexList(self) -> tuple:
		subgridIndexList = []
		for boxId in range(self.board.boxSize):
			subgridIndexList.append(self.board.getSubgridIndex(boxId))
		subgridIndexList = tuple(subgridIndexList)
		return subgridIndexList

	def getSubgridMatrixIndexList(self) -> tuple:
		subgridMatrixIndexList = []
		for boxId in range(self.board.boxSize):
			subgridIndex = self.board.getSubgridIndex(boxId)
			subgridMatrixIndexList.append(self.board.getSubgridMatrixIndex(subgridIndex))
		subgridMatrixIndexList = tuple(subgridMatrixIndexList)
		return subgridMatrixIndexList

	def getCandidatesList(self) -> tuple:
		# tuple of lists for each box
		candidatesList = []
		for i in range(self.board.boxSize):
			candidatesList.append([candidate for candidate in range(1, self.board.gridSize)])
		candidatesList = tuple(candidatesList)
		return candidatesList

	def validCandidate(self, boxValue: int, boxId: int) -> bool:
		rowIndex = self.board.getRowIndex(boxId)
		checkRow = boxValue in self.board.grid[rowIndex,:]		
		print(checkRow)
		columnIndex = self.board.getColumnIndex(boxId)
		checkColumn = boxValue in self.board.grid[:,columnIndex]
		print(checkColumn)

		subgridIndex = self.board.getSubgridIndex(boxId)
		i, j = self.board.getSubgridMatrixIndex(subgridIndex) 
		checkSubgrid = boxValue in self.board.grid[i:i+self.board.numberOfSubgrids,j:j+self.board.numberOfSubgrids]
		print(checkSubgrid)

		if checkRow and checkColumn and checkSubgrid:
			return True
		else:
			return False

	def solve(self):
		pass
