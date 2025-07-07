class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        res = []

        for i in range(0, len(numbers)):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            for j in range(i + 1, len(numbers)):
                sum = numbers[i] + numbers[j]
                if sum == target:
                    return [i + 1, j + 1]
                elif sum > target:
                    break

        return res


def main():
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([2, 3, 4], 6))
    print(solution.twoSum([-1, 0], -1))


if __name__ == "__main__":
    main()
