class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, dist):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] < dist:
                return

            grid[r][c] = dist
            up = dfs(r-1, c, dist+1)
            down = dfs(r+1, c, dist+1)
            right = dfs(r, c+1, dist+1)
            left = dfs(r, c-1, dist+1)

            # return grid[r][c]
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    dfs(row, col, 0)
        
