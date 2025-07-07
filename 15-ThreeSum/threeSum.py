# We can use the solution from 167-TwoSum2 to help us find this solution.
# Start by placing the first pointer on the left, with the second pointer
# right next to it,and the third pointer at the end of the list

# Originally I wrote a triple loop using the brute force method, but honestly
# that was way too inefficient to even keep around. NeetCode showed me how
# to solve this problem efficiently, and it made way more sense after
# listening to his explanation of the problem.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums = sorted(nums)

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append[a, nums[l], nums[r]]
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


def main():
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
    print(solution.threeSum([0, 1, 1]))
    print(solution.threeSum([0, 0, 0]))


if __name__ == "__main__":
    main()
