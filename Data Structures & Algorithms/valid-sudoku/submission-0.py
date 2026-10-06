from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = len(board)
        cols = len(board[0])

        dp_r = defaultdict(set)
        dp_c = defaultdict(set)
        squares = defaultdict(set)

        for r in range(rows):
            for c in range(cols):

                cell = board[r][c]

                if cell == ".":
                    continue
                else:
                    if cell in dp_r[r] or cell in dp_c[c] or cell in squares[(r//3, c // 3)]:
                        return  False
                    
                    dp_r[r].add(cell)
                    dp_c[c].add(cell)
                    squares[(r//3, c // 3)].add(cell)
        
        return True

                      
        