class HelpTable(object):

    def __init__(self, rules):
        result = ["Lose", "Draw", "Win"]
        amountOfMoves = len(rules.moves)
        colWidth = max(len(max(rules.moves, key=len)),
                       len(max(result, key=len))) 
        self.helpTable = [[" " for x in range(amountOfMoves + 1)]
                      for y in range(amountOfMoves + 1)]
        self.fill(0, 0, colWidth)
        for i in range(1, amountOfMoves + 1):
            for j in range(1, amountOfMoves + 1):
                self.helpTable[i][j] = result[rules.match(i - 1, j - 1) + 1]
                self.fill(i, j, colWidth)
            self.helpTable[0][i] = self.helpTable[i][0] = rules.moves[i - 1]
            self.fill(0, i, colWidth)
            self.fill(i, 0, colWidth)
        pass

    def fill(self, row, col, length):
        leftover = length - len(self.helpTable[row][col])
        for i in range(leftover):
            self.helpTable[row][col] += " "
