class Solution(object):
    def buildArray(self, nums):
        ans = []
        for i in range(len(nums)):
            ans.insert(i, nums[nums[i]])
        return ans