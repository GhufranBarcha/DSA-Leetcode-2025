class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ## Brute force
        nums.sort()
        return nums[len(nums) // 2]
        