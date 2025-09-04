''' Start by checking if a string s is of length L by doing a basic
    palindrome check algorithm (indices i,j are equivalent at each step)
    If a palindrome is not found, reduce L by 1 and try again.
    If a palindrome is not found until L=1 that substring is returned.
    An empty string will return "" '''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j) -> bool:
            left = i
            right = j - 1

            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        palindrome = ""
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start: start + length]
        return palindrome


solution = Solution()
print(solution.longestPalindrome('babad'))
print(solution.longestPalindrome('cbbd'))
print(solution.longestPalindrome('a'))
