

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
		pass

	def validCandidate(self) -> bool:
		pass

	def solve(self):
		pass
