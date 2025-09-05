class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(0, len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i+1]))
        return score


def main():
    solution = Solution()
    print(solution.scoreOfString('aa'))
    print(solution.scoreOfString('hello'))
    print(solution.scoreOfString('zaz'))


if __name__ == '__main__':
    main()
