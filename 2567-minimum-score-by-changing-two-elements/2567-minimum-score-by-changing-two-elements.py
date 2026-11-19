class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        a = heapq.nsmallest(3, nums)
        b = heapq.nlargest(3, nums)
        return min(b[0] - a[2], b[1] - a[1], b[2] - a[0])