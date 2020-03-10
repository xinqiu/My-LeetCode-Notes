class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])

        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        rot = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}

        time = 0

        while fresh:
            if not rot:
                return -1
            rot = {(i+di, j+dj) for i, j in rot
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]
                if (i+di, j+dj) in fresh}
            fresh -= rot
            time += 1
        return time