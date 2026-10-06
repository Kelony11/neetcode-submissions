# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


from collections import deque
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        ans = 0

        # NOTE: Interger comes before list

        queue = deque((x, 1) for x in nestedList)

        while queue:
            # print("queue", queue)

            x, depth = queue.popleft()
            # print("x", x, "depth", depth)

            if x.isInteger():
                ans += (x.getInteger() * depth)
            else:
                _list = x.getList()
                # New list = next depth
                nxt_depth = depth + 1

                # NOTE: ch meaning children
                for ch in _list:
                    if ch.isInteger():
                        ans += (ch.getInteger() * nxt_depth)
                    else:
                        queue.append((ch, nxt_depth))

        return ans
            


            
    
        



        
        