class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        print(nums)
        sum1 = len(nums)*(nums[0] + nums[-1])/2
        if sum1 == sum(nums):
            return False
        return True