# This solution works, but is very slow in terms of computational complexity AND memory usage.
# we could probably rewrite the 'flip' functions to not use extra arrays, and cut both down a bit.

MIN_VAL = 1
MAX_VAL = 6
TOP = 0
BOT = 1


class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        def flip_to_top(target: int) -> int:
            doms = [tops.copy(), bottoms.copy()]
            top_flips = 0
            for i in range(0, len(tops)):
                if not doms[TOP][i] == target:
                    top = doms[TOP][i]
                    doms[TOP][i] = doms[BOT][i]
                    doms[BOT][i] = top
                    top_flips += 1
            if doms[TOP].count(target) == len(tops):
                return top_flips
            else:
                return -1

        def flip_to_bottom(target: int) -> int:
            doms = [tops.copy(), bottoms.copy()]
            bot_flips = 0
            for i in range(0, len(bottoms)):
                if not doms[BOT][i] == target:
                    bot = doms[BOT][i]
                    doms[BOT][i] = doms[TOP][i]
                    doms[TOP][i] = bot
                    bot_flips += 1
            if doms[BOT].count(target) == len(tops):
                return bot_flips
            else:
                return -1

        for val in range(MIN_VAL, MAX_VAL + 1):
            tops_count = tops.count(val)
            bots_count = bottoms.count(val)
            # Now we actually can try to do the rotations
            if tops_count + bots_count >= len(tops):
                # flip the bottom row if we count less
                bot_flips = flip_to_bottom(val)
                top_flips = flip_to_top(val)
                if bot_flips >= 0 and top_flips >= 0:
                    return min(bot_flips, top_flips)
                elif top_flips >= 0:
                    return top_flips
                elif bot_flips >= 0:
                    return bot_flips
        return -1


def main():
    solution = Solution()
    print(solution.minDominoRotations([1, 2, 3], [4, 4, 4]))
    print(solution.minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]))
    print(solution.minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]))


if __name__ == "__main__":
    main()
