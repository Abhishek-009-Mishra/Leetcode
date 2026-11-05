class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        m, n = len(arr1), len(arr2)
        arr2.sort()
        ans = 0
        for num in arr1:
            idx = bisect_left(arr2, num - d)
            if idx < len(arr2) and arr2[idx] <= num + d:
                continue # Invalid
            else:
                ans += 1
        return ans   