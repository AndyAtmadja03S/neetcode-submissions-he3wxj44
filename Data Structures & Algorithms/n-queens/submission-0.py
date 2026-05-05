class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queens = []

        # checks whether the current placement
        # of a queen is valid
        def isValid(row,col):
            for r,c in enumerate(queens):
                # in the same column
                if c == col:
                    return False
                # in the same diagonal
                if abs(row - r) == abs(col -c):
                    return False
            return True
        
        def backtrack(row):
            if row == n:
                # build the board and add to results
                board = []
                for r in range(n):
                    board.append("." * queens[r] + "Q" + "." * (n - queens[r] - 1))
                res.append(board)
                return
            
            for col in range(n):
                if isValid(row, col):
                    queens.append(col)
                    backtrack(row + 1)
                    queens.pop()  # backtrack



        backtrack(0)
        return res