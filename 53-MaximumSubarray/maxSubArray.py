# I was way off base when trying to solve this myself. I thought we needed two pointers,
# or even a multi-iterative loop. The elegant solution is so simple it kind of hides in plain sight.
# sliding windows works just fine, but is very slow. we really just need to do simple addition
# on each item in the array until we reach a number that reduces our sum significantly enough
# to justify cutting it off. NeetCode's solution (again) made me feel silly.

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)

        return maxSub

    def maxSubArray_brute_sliding_window(self, nums: list[int]) -> int:
        # whole list sum
        res = sum(nums)
        i = 0
        j = len(nums)

        # now make a window and slide it over to find every sum of len() - 1 from last round.
        while i < j:
            left = i
            right = j
            while right <= len(nums):
                window_sum = sum(nums[left: right])
                if window_sum > res:
                    res = window_sum
                left += 1
                right += 1
            j -= 1

        return res

    def maxSubArray_brute(self, nums: list[int]) -> int:
        res = max(nums)

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                sub_sum = sum(nums[i: j + 1])
                if sub_sum > res:
                    res = sub_sum
        return res

    def maxSubArray_failed(self, nums: list[int]) -> int:
        res = sum(nums)
        i = 0
        j = len(nums) - 1

        while i < j:
            # check and compare the new sum to the current max
            sum_i = sum(nums[i + 1: j])
            sum_j = sum(nums[i: j + 1])

            if sum_i > sum_j:
                res = max(sum_i, res)
                j -= 1
            elif sum_i < sum_j:
                res = max(sum_j, res)
                i += 1

        return res


def main():
    solution = Solution()
    print(solution.maxSubArray([-2, 1]))
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(solution.maxSubArray([1]))
    print(solution.maxSubArray([5, 4, -1, 7, 8]))


if __name__ == "__main__":
    main()
