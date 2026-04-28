class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                print(newRow)
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        
        print(row)
        return row[0]


