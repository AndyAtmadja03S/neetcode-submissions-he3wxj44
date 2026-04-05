class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows,cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        def addRotten(r,c):
            nonlocal fresh
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] != 1:
                return
            grid[r][c] = 2
            fresh -= 1
            q.append((r,c))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row,col))
                elif grid[row][col] == 1:
                    fresh += 1
        
        mins = 0        
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                addRotten(r+1,c)
                addRotten(r-1,c)
                addRotten(r,c+1)
                addRotten(r,c-1)
            mins += 1
        return mins if fresh == 0 else -1
