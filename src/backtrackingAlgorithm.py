import sys

class backtrackingAlgorithm:

	def __init__(self, board):
		self.board = board

		self.rowIndexList = self.getRowIndexList()
		self.columnIndexList = self.getColumnIndexList()
		self.subgridIndexList = self.getSubgridIndexList()
		self.subgridMatrixIndexList = self.getSubgridMatrixIndexList()
		self.candidatesList = self.getCandidatesList()

	def getRowIndexList(self) -> tuple:
		'''returns an array containing the row index for each sudoku box'''
		rowIndexList = []
		for boxId in range(self.board.boxSize):
			rowIndexList.append(self.board.getRowIndex(boxId))
		rowIndexList = tuple(rowIndexList)
		return rowIndexList

	def getColumnIndexList(self) -> tuple:
		'''returns an array containing the column index for each sudoku box'''
		columnIndexList = []
		for boxId in range(self.board.boxSize):
			columnIndexList.append(self.board.getColumnIndex(boxId))
		columnIndexList = tuple(columnIndexList)
		return columnIndexList

	def getSubgridIndexList(self) -> tuple:
		'''returns an array containing the subgrid index for each sudoku box'''
		subgridIndexList = []
		for boxId in range(self.board.boxSize):
			subgridIndexList.append(self.board.getSubgridIndex(boxId))
		subgridIndexList = tuple(subgridIndexList)
		return subgridIndexList

	def getSubgridMatrixIndexList(self) -> tuple:
		'''returns an array containing the subgrid matrix start indecies for each sudoku box'''
		subgridMatrixIndexList = []
		for boxId in range(self.board.boxSize):
			subgridIndex = self.subgridIndexList[boxId]
			subgridMatrixIndexList.append(self.board.getSubgridMatrixIndex(subgridIndex))
		subgridMatrixIndexList = tuple(subgridMatrixIndexList)
		return subgridMatrixIndexList

	def getCandidatesList(self) -> tuple:
		'''returns a array containing an array of possible candidates for each sudoku box'''
		candidatesList = []
		for i in range(self.board.boxSize):
			candidatesList.append([candidate for candidate in range(1, self.board.gridSize+1)])
		candidatesList = tuple(candidatesList)
		return candidatesList

	def validCandidate(self, boxValue: int, boxId: int) -> bool:
		'''validates whether the current candidate meets the row, column and subgrid constraints'''
		rowIndex = self.rowIndexList[boxId]
		checkRow = boxValue not in self.board.grid[rowIndex,:]		
		#print(checkRow)
		columnIndex = self.columnIndexList[boxId]
		checkColumn = boxValue not in self.board.grid[:,columnIndex]
		#print(checkColumn)
		i, j = self.subgridMatrixIndexList[boxId]
		checkSubgrid = boxValue not in self.board.grid[i:i+self.board.numberOfSubgrids,j:j+self.board.numberOfSubgrids]
		#print(checkSubgrid)
		if checkRow and checkColumn and checkSubgrid:
			return True
		else:
			return False

	def isCandidatesListEmpty(self, boxId: int) -> bool:
		'''checks is an array containing the candidates for a sudoku box is empty'''
		return not bool(self.candidatesList[boxId])

	def refillCandidatesListIfEmpty(self, boxId: int):
		'''refills the array containing the candidates for a sudoku box if it is empty'''
		if self.isCandidatesListEmpty(boxId):
			for candidate in range(1, self.board.gridSize+1):
				self.candidatesList[boxId].append(candidate)
		else:
			pass

	def backtrack(self, boxId: int) -> int:
		'''backtracks to the first viable sudoku box from which the algorithm can continue forward'''
		boxId -= 1
		while boxId > 0:
			if self.board.fixedBoxValues[boxId]:
				boxId -= 1
			elif self.isCandidatesListEmpty(boxId):
				rowIndex, columnIndex = self.rowIndexList[boxId], self.columnIndexList[boxId]
				self.board.grid[rowIndex, columnIndex] = 0
				boxId -= 1
			else:
				break
		return boxId

	def solve(self):
		'''solves the sudoku puzzle using the backtracking algorithm'''
		currentBoxId = 0
		while currentBoxId < self.board.boxSize:
			if self.board.fixedBoxValues[currentBoxId] == 0:
				self.refillCandidatesListIfEmpty(currentBoxId)		
				while self.candidatesList[currentBoxId]:
					currentCandidate, rowIndex, columnIndex = self.candidatesList[currentBoxId][0], self.rowIndexList[currentBoxId], self.columnIndexList[currentBoxId]
					if self.validCandidate(currentCandidate, currentBoxId):
						self.board.grid[rowIndex, columnIndex] = currentCandidate
						self.candidatesList[currentBoxId].remove(currentCandidate)
						nextBoxId = currentBoxId + 1
						break
					else:
						self.candidatesList[currentBoxId].remove(currentCandidate)
						if self.isCandidatesListEmpty(currentBoxId):
							rowIndex, columnIndex = self.rowIndexList[currentBoxId], self.columnIndexList[currentBoxId]
							self.board.grid[rowIndex, columnIndex] = 0
							nextBoxId = self.backtrack(currentBoxId)
						else:
							pass
				currentBoxId = nextBoxId
			else: 
				currentBoxId += 1
			