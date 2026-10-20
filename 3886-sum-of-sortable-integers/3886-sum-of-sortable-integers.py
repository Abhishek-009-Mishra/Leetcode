class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)

        def check(k):
            prev = 0

            for i in range(0, n, k):
                block = nums[i:i + k]
                cnt = sum(
                    block[j] > block[j + 1]
                    for j in range(k - 1)
                )

                if block[-1] > block[0]:
                    cnt += 1

                if cnt > 1 or prev > min(block):
                    return False

                prev = max(block)

            return True

        ans = 0

        for k in range(1, int(n**0.5) + 1):
            if n % k == 0:
                if check(k):
                    ans += k

                other = n // k
                if other != k and check(other):
                    ans += other

        return ans