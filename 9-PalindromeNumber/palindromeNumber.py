''' Strangely enough, the LeetCode problem asked if we could solve the palindrome problem without
    casting to a string. when we did so, we discovered that (at least with Python) the string solution
    was actually faster than the integer solution. Probably due to all the division?
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        div = 1
        while x >= div * 10:
            div *= 10

        while x:
            right = x % 10
            left = x // div

            if left != right:
                return False

            x = (x % div) // 10
            div /= 100
        return True

    def isPalindromeStringVersion(self, x: int) -> bool:
        def is_string_palindrome(s: str) -> bool:
            left = 0
            right = len(s) - 1

            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        return is_string_palindrome(str(x))


def main():
    solution = Solution()
    arg1, arg2, arg3, arg4, arg5 = 0, 121, -121, 10, 1221
    print(solution.isPalindromeStringVersion(arg1))
    print(solution.isPalindromeStringVersion(arg2))
    print(solution.isPalindromeStringVersion(arg3))
    print(solution.isPalindromeStringVersion(arg4))
    print(solution.isPalindromeStringVersion(arg5))
    print(solution.isPalindrome(arg1))
    print(solution.isPalindrome(arg2))
    print(solution.isPalindrome(arg3))
    print(solution.isPalindrome(arg4))
    print(solution.isPalindrome(arg5))


if __name__ == "__main__":
    main()
