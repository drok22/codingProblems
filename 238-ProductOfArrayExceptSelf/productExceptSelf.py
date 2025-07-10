from testCase import large_data


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ''' This function temporarily store the first pass prefix values in the result array.
            The second pass goes through the result array backwards and applies the postfix values.
            after 2 passes, we've saved memory by storing in a single array.
            We have also saved time by only doing 2 passes.
        '''
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

    def productExceptSelf_SLOW(self, nums: list[int]) -> list[int]:
        ''' This function solves the problem, but at the cost of time
        '''
        res = []
        for i in range(0, len(nums)):
            n = 1
            for j in range(0, len(nums)):
                if i == j:
                    continue
                else:
                    n *= nums[j]
            res.append(n)
            i += 1
        return res


def main():
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4]))
    print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
    print(solution.productExceptSelf([2, 4, 6, 8, 10]))
    print(solution.productExceptSelf(large_data))


if __name__ == "__main__":
    main()
