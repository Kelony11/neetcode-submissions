# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # Get to the middle of the LL

        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            print('slow.val', slow.val)

            fast = fast.next.next
            # print('fast.val', fast.val)

        # Reverse the second half
        prev = None
        while slow:
            next_node = slow.next

            slow.next = prev

            prev = slow
            slow = next_node
        
        # print("prev.val", prev.val)

        # Traversing in opposite direction

        ans = 0

        first, end = head, prev 
        while first and first.next:
            # print("first.val", first.val)
            ans = max(ans, first.val + end.val)
            first = first.next
            end = end.next

        return ans

    




        