
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)

        ans = 0
        cost = 0

        dq = deque()

        j = n - 1

        for i in range(n - 1, -1, -1):

            while dq and nums[dq[-1]] < nums[i]:

                l = dq.pop()

                r = j + 1 if not dq else dq[-1]

                cost += (r - l) * (nums[i] - nums[l])

            dq.append(i)

            while cost > k:

                cost -= nums[dq[0]] - nums[j]

                if dq[0] == j:
                    dq.popleft()

                j -= 1

            ans += j - i + 1

        return ans