class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s)>k:
            ts = []
            for i in range(0,len(s),k):
                group = s[i:i+k]
                summ = sum(int(digit) for digit in group)
                ts.append(str(summ))
            s = "".join(ts)
        return s