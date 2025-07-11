class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """ Do not return anything, modify matrix in-place instead.
        """
        left = 0
        right = len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top = left
                bottom = right

                # Save top left value
                top_left = matrix[top][left + i]

                # move bottom left into top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # move bottom right into bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # move top right into bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # move top left into top right
                matrix[top + i][right] = top_left
            right -= 1
            left += 1


def main():
    solution = Solution()
    print(solution.rotate([[1, 2, 3],    # 7, 4, 1
                           [4, 5, 6],    # 8, 5, 2
                           [7, 8, 9]]))  # 9, 6, 3

    print(solution.rotate([[5, 1, 9, 11],       # 15, 13,  2,  5
                           [2, 4, 8, 10],       # 14,  3,  4,  1
                           [13, 3, 6, 7],       # 12,  6,  8,  9
                           [15, 14, 12, 16]]))  # 16,  7, 10, 11

    print(solution.rotate([]))
    print(solution.rotate([]))


if __name__ == "__main__":
    main()
