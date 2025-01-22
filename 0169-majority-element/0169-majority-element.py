class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ## Brute force
        # nums.sort()
        # return nums[len(nums) // 2]

        count = 0
        n = None

        for num in nums:
            if count == 0:
                n = num

            count += 1 if num  == n else -1
        return n      

        