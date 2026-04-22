class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if ((r < 0 or r >= rows) or
               (c < 0 or c >= cols) or
               (grid[r][c] == 0)):
                    return 0
            grid[r][c] = 0
            down = dfs(r + 1, c)
            up = dfs(r - 1, c)
            right = dfs(r, c + 1)
            left = dfs(r, c - 1)

            return 1 + down+up+right+left
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    tot = dfs(r, c)
                    area = max(tot, area)
        return area            
            