class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]

        rank = [1 for i in range(n)]

        def find_parent(n):
            p = n
            while p != parent[n]:
                parent[n] = parent[parent[n]]
                p = parent[n]
            return p


        def union(node1, node2):
            p1, p2 = find_parent(node1), find_parent(node2)

            if p1 == p2:
                return 0

            if rank[p1] > rank[p2]:
                parent[p2] = p1 #Father
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2 #Father
                rank[p2] += rank[p1]

            return 1

        num_components = n
        for n1, n2 in edges:
            num_components -= union(n1, n2)

        return num_components




        