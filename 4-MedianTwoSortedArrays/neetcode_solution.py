'''
4. Median of two sorted arrays

This one requires a binary search to solve it the fastest and using the least memory
https://www.youtube.com/watch?v=q6IEA26hvXc
'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total // 2

        # swap names if b is longer
        if len(b) < len(a):
            a, b = b, a

        left, right = 0, len(a) - 1
        while True:
            i = (left + right) // 2  # a
            j = half - i - 2  # b

            aleft = a[i] if i >= 0 else float("-infinity")
            aright = a[i + 1] if (i + 1) < len(a) else float("infinity")
            bleft = b[j] if j >= 0 else float("-infinity")
            bright = b[j + 1] if (j + 1) < len(b) else float("infinity")

            # partition is correct
            if aleft <= bright and bleft <= aright:
                # odd
                if total % 2:
                    return min(aright, bright)
                else:  # even
                    return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                right = i - 1
            else:
                left = i + 1


def main():
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 3], [2]))  # Output: 2.0
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5


if __name__ == "__main__":
    main()
