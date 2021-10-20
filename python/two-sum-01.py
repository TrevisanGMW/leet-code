# https://leetcode.com/problems/two-sum/
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

            if pair_num in num_map:
                return [num_map.get(pair_num), i]
            
            num_map[nums[i]] = i

# # Local Test
# import timeit

# def local_test():
#         run_obj = Solution()
#         run_obj.twoSum([3,2,3], 6)

# def time_test():
#     #trials = 10_000_000
#     trials = 1_000_000
#     kwargs = {'setup' : 'x=42',
#               'globals' : globals(), 
#               'number': trials}

#     time_output = timeit.timeit('local_test()', **kwargs)
#     print(f'{time_output=:.02f}')

# if __name__ == '__main__':
#     #local_test() # expected [0,2]
#     time_test()
    

# Results
# 08/08/2021 20:59	Accepted	40 ms	14.4 MB	python
# 08/21/2021 09:34	Accepted	72 ms	14.4 MB	python (54.38%)
# Solution: Hashmaps