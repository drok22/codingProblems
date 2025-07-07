''' Trapping Rain Water:
    https://leetcode.com/problems/trapping-rain-water/
    https://www.youtube.com/watch?v=ZI2z5pq0TqA
'''


class Solution:
    def trap(self, height: list[int]) -> int:
        total = 0
        i: int = 0
        j: int = len(height) - 1
        max_l = height[i]
        max_r = height[j]

        while i < j:

            if max_l <= max_r:
                amount = max_l - height[i]
                if amount > 0:
                    total += amount
                i += 1
                max_l = max(height[i], max_l)

            else:
                amount = max_r - height[j]
                if amount > 0:
                    total += amount
                j -= 1
                max_r = max(height[j], max_r)

        return total


solution = Solution()
print(solution.trap([4, 2, 3]))  # first failed test. algorithm doesn't recognize that middle will hold water...
print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(solution.trap([4, 2, 0, 3, 2, 5]))
