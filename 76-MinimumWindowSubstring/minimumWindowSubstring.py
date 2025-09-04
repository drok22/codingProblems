class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        count_t = {}
        window = {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)
        have = 0
        need = len(count_t)
        res = [-1, -1]
        res_len = float('infinity')
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)
            if c in count_t and window[c] == count_t[c]:
                have += 1
            while have == need:
                # update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = (right - left + 1)
                # pop from the left of our window
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1

        left, right = res
        return s[left: right + 1] if res_len != float('infinity') else ''


def main():
    solution = Solution()
    print(solution.minWindow("ADOBECODEBANC", "ABC"))
    print(solution.minWindow("a", "a"))
    print(solution.minWindow("a", "aa"))


if __name__ == "__main__":
    main()
