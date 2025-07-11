# classic 'get the next digit from an integer n problem. Could have used a string solution
# but decided to try it the % and // way. we solve by converting the number to its digit
# components in a list, and then get the sum of the squares of each digit, then add it
# to a hash map of sums we have calculated during the process. If we reach 1(True) or hit a
# collision in the hash map(False), we are done checking whether or not the number is 'happy'

class Solution:
    def isHappy(self, n: int) -> bool:
        used_sums = []

        while n:
            digits = []
            while n:
                next = n % 10
                n = n // 10
                digits.append(next)

            sum = 0
            for digit in digits:
                sum += digit ** 2

            if sum == 1:
                return True
            elif sum in used_sums:
                return False
            used_sums.append(sum)
            n = sum
        return False


def main():
    solution = Solution()
    print(solution.isHappy(19))
    print(solution.isHappy(2))


if __name__ == "__main__":
    main()