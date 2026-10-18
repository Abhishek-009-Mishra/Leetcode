import math

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        def get_ways(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            ways = math.comb(len(left) + len(right), len(left))
            return (ways * get_ways(left) * get_ways(right)) % MOD
            
        return (get_ways(nums) - 1) % MOD    