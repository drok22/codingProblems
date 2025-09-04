class Solution:
    def numberToWords(self, num: int) -> str:
        words = ''

        while num:
            digit = num % 10
            num = num // 10

            print(f'digit: {digit}')
            print(f'next num: {num}')

            words = convert(digit) + words

        return ''


def convert(d: int) -> str:
    match d:
        case 1:
            return 'One'
        case 2:
            return 'Two'
        case 3:
            return 'Three'
        case 4:
            return 'Four'
        case 5:
            return 'Five'
        case 6:
            return 'Six'
        case 7:
            return 'Seven'
        case 8:
            return 'Eight'
        case 9:
            return 'Nine'


def main():
    solution = Solution()
    print(solution.numberToWords(123))
    print(solution.numberToWords(12345))
    print(solution.numberToWords(1234567))


if __name__ == "__main__":
    main()