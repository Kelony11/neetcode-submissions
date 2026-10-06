class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):

        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        
        return x

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)

        if pa == pb:
            return False 

        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
        elif self.rank[pb] > self.rank[pa]:
            self.parent[pa] = pb
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1

        # print("self.parent", self.parent)
        # print("self.rank", self.rank)
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for u, v in sorted(edges, key=lambda x:x[0]):
            # print("u", u, "v", v)
            if uf.union(u, v):
                # Each time two nodes merges, n get deducted
                # eg. n = 3  (0 -> 0) -> 0
                # if (0 -> 0), n - 1 = 2, 2 nodes are left
                n -= 1

        return n
            
        