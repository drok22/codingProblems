# I was pleasantly surprised to see that my time complexity score was very good for this solution (100%)
# Space complexity was not quite as good (24%)

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        reordered = []
        dig = []
        # identify log types
        for log in logs:
            split_log = log.split(' ')

            if split_log[1].isnumeric():
                dig.append(log)
            else:
                reordered.append(log)
        # sort the alphabetical logs lexicographically
        # the lambda is the same as calling s.split(' ') and then taking the second
        # element of each log and sorting them separately
        reordered = sorted(reordered, key=lambda s: (s.split(' ', 1)[1], s.split(' ', 1)[0]))
        # reordered = sort_alphabetical_logs(reordered)
        # add back the digit logs to end of the sorted logs
        for log in dig:
            reordered.append(log)

        return reordered


def main():
    solution = Solution()
    print(solution.reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo", "a2 act car"]))
    print(solution.reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
    print(solution.reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))


if __name__ == "__main__":
    main()
