'''
https://leetcode.com/problems/word-search/
https://www.youtube.com/watch?v=pfiQ_PS1g8E
'''


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def depth_first_search(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            path.add((r, c))
            res = (depth_first_search(r + 1, c, i + 1) or
                   depth_first_search(r - 1, c, i + 1) or
                   depth_first_search(r, c + 1, i + 1) or
                   depth_first_search(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if depth_first_search(r, c, 0):
                    return True
        return False


solution = Solution()
print(solution.exist([["A", "B", "C", "E"],
                      ["S", "F", "C", "S"],
                      ["A", "D", "E", "E"]], "ABCCED"))

print(solution.exist([["A", "B", "C", "E"],
                      ["S", "F", "C", "S"],
                      ["A", "D", "E", "E"]], "SEE"))

print(solution.exist([["A", "B", "C", "E"],
                      ["S", "F", "C", "S"],
                      ["A", "D", "E", "E"]], "ABCB"))
