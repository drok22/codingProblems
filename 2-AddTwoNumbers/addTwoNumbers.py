# Haven't written linked list code since college C++ class. Lets give it a go
# Definition for singly-linked list.
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_node = ListNode()
        cur = dummy_node

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_node.next


def main():
    _ = Solution()


if __name__ == "__main__":
    main()
