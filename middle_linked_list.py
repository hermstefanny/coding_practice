from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:

            return head

        end = head
        middle = head

        while end and end.next:
            middle = middle.next
            end = end.next.next

        return middle


linked_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
solution = Solution()
print(solution.middleNode(linked_1))
