NEIGBOR_MAP = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """ Do not return anything, modify board in-place instead.
        """
        def check_neighbors(i, j) -> int:
            ''' Count neighbors of the current square and check their live/dead status.
                Increment live_neighbors for each 1 found and return the count.
            '''
            live_neighbors = 0
            for row, col in NEIGBOR_MAP:
                n_row = i + row
                n_col = j + col
                if ((n_row >= 0 and n_row < len(board)) and (n_col >= 0 and n_col < len(board[0]))):
                    if board[n_row][n_col] == 1:
                        live_neighbors += 1
            return live_neighbors

        change_list = []
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                cell = board[i][j]
                live_neighbors = check_neighbors(i, j)
                if cell == 0 and live_neighbors == 3:
                    change_list.append((i, j))
                elif cell == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    change_list.append((i, j))
        for i, j in change_list:
            entry = board[i][j]
            board[i][j] = 1 if entry == 0 else 0


def main():
    solution = Solution()
    print(solution.gameOfLife([[0, 1, 0],     # [0,0,0]
                               [0, 0, 1],     # [1,0,1]
                               [1, 1, 1],     # [0,1,1]
                               [0, 0, 0]]))   # [0,1,0]
    print(solution.gameOfLife([[1, 1],
                               [1, 0]]))
    print(solution.gameOfLife([[0, 0, 0],
                               [1, 0, 1],
                               [0, 1, 1],
                               [0, 1, 0]]))
    print(solution.gameOfLife([[1, 1],
                               [1, 1]]))


if __name__ == "__main__":
    main()
