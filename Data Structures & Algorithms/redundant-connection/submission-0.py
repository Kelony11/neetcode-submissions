class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)

        parent = [i for i in range(n + 1)]
        # print("parent", parent)
        rank = [0] * (n + 1)
        # print("rank", rank)

        def find(x):
            print("x", x)

            if x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):

            pa, pb = find(a), find(b)

            if find(a) == find(b):
                return False

            if rank[pa] > rank[pb]:
                parent[pb] = pa
            elif rank[pb] > rank[pa]:
                parent[pa] = pb
            else:
                parent[pb] = pa
                rank[pa] += 1
            
            return True
        
        for u, v in edges:
            if not union(u,v):
                return [u,v]
        


        