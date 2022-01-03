class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        
        n = len(nums)
        nums.sort()
        sols = set()
        for i in range(1, n - 1):
            l = i - 1
            r = i + 1
            
            while l >= 0 and r < n:
                s = nums[l] + nums[i] + nums[r]

                if s > 0:
                    l -= 1
                elif s < 0:
                    r += 1
                else:
                    sols.add((nums[l], nums[i], nums[r]))
                    l -= 1
                    r += 1

        return list(sols)
        