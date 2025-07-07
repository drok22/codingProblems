''' https://www.youtube.com/watch?v=pV2kpPD66nE
    https://leetcode.com/problems/3sum/
'''
import collections


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        # Breadth-First Search
        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for (dr, dc) in directions:
                    r = row + dr
                    c = col + dc

                    if (r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands


def main():
    solution = Solution()
    print(solution.numIslands([["1", "1", "1", "1", "0"],
                               ["1", "1", "0", "1", "0"],
                               ["1", "1", "0", "0", "0"],
                               ["0", "0", "0", "0", "0"]]))
    print(solution.numIslands([["1", "1", "0", "0", "0"],
                               ["1", "1", "0", "0", "0"],
                               ["0", "0", "1", "0", "0"],
                               ["0", "0", "0", "1", "1"]]))


if __name__ == "__main__":
    main()
