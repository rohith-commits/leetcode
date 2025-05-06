class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[len(nums)-k : len(nums)] + nums[:len(nums)-k]
        
        