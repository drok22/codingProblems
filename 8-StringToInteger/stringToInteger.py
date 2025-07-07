''' https://leetcode.com/problems/string-to-integer-atoi/

    This solution feels messy, but works. I don't like how many continues there are,
    and don't really like using loop breaks. In this case, it felt like the thing to do.
'''


class Solution():
    def myAtoi(self, s: str) -> int:
        MIN = -2147483648
        MAX = 2147483647
        n = 0
        is_neg = False
        only_read_nums = False

        for char in s:
            if not only_read_nums:
                if char == ' ':
                    continue
                elif char == '-':
                    is_neg = True
                    only_read_nums = True
                    continue
                elif char == '+':
                    only_read_nums = True
                    continue

            if char.isnumeric():
                only_read_nums = True
                if n == 0:
                    n = int(char)
                else:
                    n = (n * 10) + int(char)
            else:
                break

        if is_neg:
            n *= -1

        if n <= MIN:
            return MIN
        if n >= MAX:
            return MAX
        return n


solution = Solution()

print(solution.myAtoi("42"))
print(solution.myAtoi("   -042"))
print(solution.myAtoi("1337c0d3"))
print(solution.myAtoi("0-1"))
print(solution.myAtoi("words and 987"))
print(solution.myAtoi("-2147483648"))
print(solution.myAtoi("2147483647"))
