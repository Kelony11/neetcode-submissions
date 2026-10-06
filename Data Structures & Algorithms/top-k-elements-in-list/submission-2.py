class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_map = {}

        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        print(hash_map)


        values = []
        for item in hash_map:
            values.append((item, hash_map[item]))

        values.sort(key=lambda x: x[-1], reverse=True)

        result = []
        for key, values in values:
            result.append(key)

        return result[:k]
            
            




        