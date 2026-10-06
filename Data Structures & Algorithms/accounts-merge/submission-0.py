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
            
        return True 

from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        uf = UnionFind(len(accounts))

        email_to_id = defaultdict(int)

        for idx, cred in enumerate(accounts):
            # print("idx", idx, "cred", cred)
            for email in cred[1:]:
                # print("email", email)
                # print("email_to_id", email_to_id)
                if email in email_to_id:
                    # print("???", email_to_id[email])
                    uf.union(idx, email_to_id[email])
                else:
                    email_to_id[email] = idx

        # print("final email_to_id", email_to_id)

        id_to_emails = defaultdict(list)

        for e, idx in email_to_id.items():
            father = uf.find(idx)

            id_to_emails[father].append(e)

        ans = []

        for idx, emails in id_to_emails.items():
            name = accounts[idx][0]

            ans.append([name] + sorted(emails))

        return ans
                

        
        
            


