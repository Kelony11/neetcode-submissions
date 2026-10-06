class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = 0, 0

        while True:

            # RANDOMIZE SLOW AND FAST UNTIL THEY MATCH 
            slow = nums[slow]
            # print("slow", slow)
            fast = nums[nums[fast]]
            # print("fast", fast)

            if slow == fast:
                # print("slow", slow)
                break

        confirm = 0

        while True:
            confirm = nums[confirm]
            slow = nums[slow]

            if slow == confirm:
                return confirm

        
        
        

        