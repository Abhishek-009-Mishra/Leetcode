class Solution {
public:
    int maximumLength(vector<int>& nums) {
        unordered_map<long long, int> cnt;

        for (int x : nums)
            cnt[x]++;

        int ans = 1;

        if (cnt.count(1))
            ans = cnt[1] - (cnt[1] % 2 == 0);

        for (auto &[x, f] : cnt) {

            if (x == 1)
                continue;

            long long cur = x;
            int len = 0;

            while (cnt.count(cur) && cnt[cur] >= 2) {
                len += 2;

                if (cur > 1000000000LL)
                    break;

                cur *= cur;
            }

            if (cnt.count(cur))
                len++;
            else
                len--;

            ans = max(ans, len);
        }

        return ans;
    }
};