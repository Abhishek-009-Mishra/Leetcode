#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

#define ordered_set tree<int, null_type,less_equal<int>, rb_tree_tag,tree_order_statistics_node_update>


class Solution {
public:
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        int n = nums.size(); 
        vector<long long> pref(n + 1,0); 
        for(int i = 0; i < n; i++) {
            // nums[i] = (nums[i] == target ? 1 : 0);  we make target = 1, rest = 0, as we don't care about values 
            pref[i + 1] = pref[i] + (nums[i] == target ? 1: 0); 
        }
        
        // Now what I have to do? 
        // 0 1 1 0 
        // 0 0 1 2 2 -> pref array 
        // for any [i, j] -> total how many times appeared ? pref[j + 1] - pref[i] 
        // so if f(i, j) = 2 * (pref[j + 1] - pref[i]) > j - i + 1 if true it will be added to answer as for majority strictly greater than half of length 
        // since at any point i can be fixed -> we only need to find the P(j) valid values out of it. 

        // this clearly gives us idea abour -> reverse and use ordered set to find values > than current. 

        // equation 2 * P[j + 1] - j > 2 * P[i] - i + 1 
        ordered_set os; 
        long long ans = 0; 
        os.insert(2 * pref[n] - n); // insert the last value 

        for (int i = n - 1; i >= 0; i--) {
            long long x = 2 * pref[i] - i;

            long long req = os.size() - os.order_of_key(x + 1);
            ans += req;

            os.insert(x);
        }
        return ans; 
    }   
};