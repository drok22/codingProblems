# NeetCode has shown me over and over that its possible to solve most of these problems using
# two pointers, starting at each end of the array. Try thinking this way more often if possible.

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers - 1)
        while l - r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []


def main():
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([2, 3, 4], 6))
    print(solution.twoSum([-1, 0], -1))


if __name__ == "__main__":
    main()
