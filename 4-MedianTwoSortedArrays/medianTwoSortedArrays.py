''' I added the arrays together, sorted them.
    Found the middle two pointers based on even/odd len()
    averaged the value of those two locations and returned the answer.
    according to leetCode, the actual time was not THAT slow,
    but it used more memory than other solutions.

    A better solution would be to use a binary search instead.
'''


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        median: float = 0.0
        # merge list
        new_nums: list = nums1 + nums2
        new_nums.sort()
        list_len: int = len(new_nums)
        middle_loc: int = list_len % 2

        if middle_loc == 0:  # even len
            m1 = new_nums[int((list_len / 2) - 1)]
            m2 = new_nums[int((list_len / 2))]
            median = (m1 + m2) / 2
        else:  # odd len
            odd_loc = int(list_len / 2)
            print(f'odd_loc: {odd_loc}')
            median = new_nums[odd_loc]

        return median
