class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        re = 0
        f = [0] * 26

        l = 0
        for r in range(n):
            f[ord(s[r]) - ord('a')] += 1

            while f[ord(s[r]) - ord('a')] > 2:
                f[ord(s[l]) - ord('a')] -= 1
                l += 1

            re = max(re, r-l+1)

        return re