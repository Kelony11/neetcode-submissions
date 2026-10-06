class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0

        hash_set = set()
        hash_set.add(nums[i])

        for j in range(1, len(nums)):
            # print("j++", j)

            while i < j and abs(i - j) > k:
                hash_set.remove(nums[i])
                # print(f"removed {nums[i]} from hashset {hash_set}")
                i += 1
                # print("i++", i)

            if i < j and nums[j] in hash_set:
                return True
            
            hash_set.add(nums[j])
            # print(f"added {nums[j]} to hash_set", hash_set)

        return False
            

            



        