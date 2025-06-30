''' Find the longest palindrome inside of a given string.

    The main idea for validating a palindrome as a string is to set a pointer
    at the start and end of the string. if theyr'e matching characters, we move
    the start pointer forward and the end pointer backward, and compare again.
    If we make it to the point they meet or start > end we are done comparing.
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ''' A simple function to validate if a string is a palindrome.
            Compares the pointer values to each other. if they match,
            move them to the next character inside of the substring until
            the pointers meet.
        '''
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
        # set pointer at end of the string, move it backward each iter
        for length in range(len(s), 0, -1):
            # set pointer at beginning of the string, move it forward each iter
            for start in range(len(s) - length + 1):
                # check substring created by index pointers and return if its validated
                if check(start, start + length):
                    return s[start: start + length]
        return palindrome


solution = Solution()
print(solution.longestPalindrome('babad'))
print(solution.longestPalindrome('cbbd'))
