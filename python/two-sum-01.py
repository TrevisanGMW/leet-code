class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        num_map = {} # Using a dictionary as a hash table for speed
        
        for i in range(len(nums)):
            pair_num = target - nums[i]

            print(nums[i])
            if pair_num in num_map:
                return [num_map.get(pair_num), i]
            
            num_map[nums[i]] = i

# Local Test
# if __name__ == '__main__':
#     run_obj = Solution()
#     print(run_obj.twoSum([3,2,3], 6)) # expected [0,2]

# Results
# 08/08/2021 20:59	Accepted	40 ms	14.4 MB	python
# Solution: Hashmaps