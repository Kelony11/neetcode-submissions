# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        curr = head

        arr = [curr.val if curr else 0]

        while curr and curr.next:
            curr = curr.next
            # print('curr.val', curr.val)

            arr.append(curr.val if curr else 0)

        # print("final arr", arr)

        l, r = 0, len(arr) - 1

        ans = 0

        while l < r:
            ans = max(ans, arr[l] + arr[r])
            l += 1
            r -= 1
        
        return ans





        