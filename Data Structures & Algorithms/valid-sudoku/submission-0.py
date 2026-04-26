class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                box_index = ((r//3)*3) + (c//3)
                item = board[r][c]
                if item == ".":
                    continue
                if item in rows[r] or item in cols[c] or item in boxs[box_index]:
                    return False
                else:
                    rows[r].add(item)
                    cols[c].add(item)
                    boxs[box_index].add(item)
        return True
        