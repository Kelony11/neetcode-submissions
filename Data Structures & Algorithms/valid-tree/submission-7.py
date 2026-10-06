import heapq
from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:















































        

        if not n:
            return True 

        adj_list = defaultdict(list) 
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        #         parent, current node
        min_heap = [(-1, 0)]
        visited = set()
        visited.add(0)

        while min_heap:
            parent_node, curr_node = heapq.heappop(min_heap)

            for neighbor in adj_list[curr_node]:

                if neighbor == parent_node:
                    continue

                if neighbor in visited:
                    return False

                visited.add(neighbor)
                heapq.heappush(min_heap, (curr_node, neighbor))

            
        return len(visited) == n



                



            



        