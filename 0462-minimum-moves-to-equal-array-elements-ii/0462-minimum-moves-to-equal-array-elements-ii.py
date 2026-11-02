class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        change=nums[len(nums)//2]
        return sum(abs(change-num) for num in nums)