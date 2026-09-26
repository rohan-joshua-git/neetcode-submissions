class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                b = (i//3)*3 + j//3

                if (val in row[i]) or (val in column[j]) or (val in box[b]):
                    return False
                else:
                    row[i].add(val)
                    column[j].add(val)
                    box[b].add(val)
        return True
