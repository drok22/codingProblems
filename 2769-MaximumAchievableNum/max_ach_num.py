class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        max = 0
        low = num - (t*2) if num - (t*2) > 0 else 0
        high = num + (t*2)

        for i in range(low, high + 1):
            if is_achievable(num, t, i):
                print(f'{i} is achievable')
                max = i
            else:
                print(f'{i} is NOT achievable')
        return max


def is_achievable(num: int, t: int, x: int) -> bool:
    # Using Math:
    if abs(num - x) % 2 == 0:
        return True
    else:
        return False
    # Using Brute Force:
    while t > 0:
        if x > num:
            x -= 1
            num += 1
        elif x < num:
            x += 1
            num -= 1
        if x == num:
            return True
        t -= 1
    return False


def main():
    solution = Solution()
    print(solution.theMaximumAchievableX(4, 1))
    print(solution.theMaximumAchievableX(3, 2))


if __name__ == '__main__':
    main()
