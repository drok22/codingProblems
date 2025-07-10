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
        # sorting the array allows us to skips some enumerations later
        nums = sorted(nums)

        for i, a in enumerate(nums):
            # if i is the same as the value in front of it, we can skip it in the future
            if i > 0 and a == nums[i - 1]:
                continue
            # this loop will be largely the same as the 2Sum2 solution which uses pointers at opposite ends
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res


def main():
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
    print(solution.threeSum([0, 1, 1]))
    print(solution.threeSum([0, 0, 0]))


if __name__ == "__main__":
    main()
