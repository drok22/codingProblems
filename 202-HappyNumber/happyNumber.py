# classic 'get the next digit from an integer n problem. Could have used a string solution
# but decided to try it the % and // way. we solve by converting the number to its digit
# components in a list, and then get the sum of the squares of each digit, then add it
# to a hash map of sums we have calculated during the process. If we reach 1(True) or hit a
# collision in the hash map(False), we are done checking whether or not the number is 'happy'

class Solution:
    def isHappy(self, n: int) -> bool:
        # list of sums that have been checked for happy num status
        used_sums = []
        while n:
            digits = []
            # mod to get the rightmost digit, then floor division to 'chop' it off
            while n:
                next = n % 10
                n = n // 10
                digits.append(next)
            # Calculate the sum of the squares of each digit
            sum = 0
            for digit in digits:
                sum += digit ** 2
            # A happy number can eventually be reduced to exactly one after a few loops
            if sum == 1:
                return True
            # An unhappy number will find itself in an infinite loop. as soon as we
            # hit the same sum twice, we know we will never exit the loop naturally
            elif sum in used_sums:
                return False
            used_sums.append(sum)
            # After we update the checked sums, begin next loop with recently calculated sum
            n = sum
        return False


def main():
    solution = Solution()
    print(solution.isHappy(19))
    print(solution.isHappy(2))


if __name__ == "__main__":
    main()
