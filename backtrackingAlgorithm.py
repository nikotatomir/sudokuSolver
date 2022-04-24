import sys

class backtrackingAlgorithm:

	def __init__(self, board):
		self.board = board

		self.rowIndexList = self.getRowIndexList()
		self.columnIndexList = self.getColumnIndexList()
		#self.subgridIndexList = self.getSubgridIndexList()
		self.subgridMatrixIndexList = self.getSubgridMatrixIndexList()
		self.candidatesList = self.getCandidatesList()

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

	# def getSubgridIndexList(self) -> tuple:
	# 	subgridIndexList = []
	# 	for boxId in range(self.board.boxSize):
	# 		subgridIndexList.append(self.board.getSubgridIndex(boxId))
	# 	subgridIndexList = tuple(subgridIndexList)
	# 	return subgridIndexList

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
			candidatesList.append([candidate for candidate in range(1, self.board.gridSize+1)])
		candidatesList = tuple(candidatesList)
		return candidatesList

	def validCandidate(self, boxValue: int, boxId: int) -> bool:
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

	def isCandidatesListEmpty(self, boxId):
		return not bool(self.candidatesList[boxId])

	def backtrack(self, boxId):
		# rowIndex, columnIndex = self.rowIndexList[boxId], self.columnIndexList[boxId]
		# self.board.grid[rowIndex, columnIndex] = 0
		boxId -= 1
		while boxId > 0:
			print('BACKTRACK', self.board.grid)
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
		currentBoxId = 0
		while currentBoxId < 81:
			print('currentBoxId ->', currentBoxId)
			if self.board.fixedBoxValues[currentBoxId] == 0:
				
				if self.isCandidatesListEmpty(currentBoxId):
					for candidate in range(1, self.board.gridSize+1):
						self.candidatesList[currentBoxId].append(candidate)
				else:
					pass

				while self.candidatesList[currentBoxId]:
					currentCandidate, rowIndex, columnIndex = self.candidatesList[currentBoxId][0], self.rowIndexList[currentBoxId], self.columnIndexList[currentBoxId]
					print ('CURRENT CANDIDATE ->', currentCandidate)
					if self.validCandidate(currentCandidate, currentBoxId):
						self.board.grid[rowIndex, columnIndex] = currentCandidate
						print(self.board.grid)
						self.candidatesList[currentBoxId].remove(currentCandidate)
						nextBoxId = currentBoxId + 1
						# sys.exit('EXIT')
						break

					else:
						self.candidatesList[currentBoxId].remove(currentCandidate)
						if self.isCandidatesListEmpty(currentBoxId):
							print('note', self.candidatesList[currentBoxId])
							rowIndex, columnIndex = self.rowIndexList[currentBoxId], self.columnIndexList[currentBoxId]
							self.board.grid[rowIndex, columnIndex] = 0
							nextBoxId = self.backtrack(currentBoxId)

							# nextBoxId = currentBoxId - 1
							# while self.board.fixedBoxValues[nextBoxId] != 0 or not self.candidatesList[nextBoxId]:
							# 	nextBoxId -= 1
						else:
							pass
				
				currentBoxId = nextBoxId
			
			else: 
				currentBoxId += 1
			