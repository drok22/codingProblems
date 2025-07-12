class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        res = []
        prev_interval = None
        # sorting the list first adds some time but makes this algorithm run a lot smoother.
        intervals.sort(key=lambda i: (i[0]))
        # hold onto the previous interval and compare it to the next interval. If they overlap, merge them and add to the result
        # reset the previous interval to the added interval before the loop restarts to check if that interval also overlaps.
        for interval in intervals:
            # set the previous interval on the first loop iteration
            if not prev_interval:
                prev_interval = interval
            else:
                # if an interval overlaps, we combine the current interval and the previous interval.
                if min(interval) <= max(prev_interval):
                    prev_interval = [min(min(prev_interval), min(interval)), max(max(prev_interval), max(interval))]
                # when the intervals don't overlap, add the previous interval to the result and compare the next interval set.
                else:
                    res.append(prev_interval)
                    prev_interval = interval
        # when the loop closes, we will be holding onto the last interval and need to add it to the result.
        res.append(prev_interval)
        return res


def main():
    solution = Solution()
    print(solution.merge([[1, 4], [0, 0]]))
    print(solution.merge([[1, 4], [0, 4]]))
    print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(solution.merge([[1, 4], [4, 5]]))


if __name__ == "__main__":
    main()
