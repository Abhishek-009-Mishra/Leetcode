class Solution {
public:
    int maxNumberOfBalloons(string s) {
       unordered_map<char,int>mp,mp2;
        for(char ch:s)mp[ch]++;
        int ans=INT_MAX;
        string target="balloon";
        for(char ch:target){
           mp2[ch]++;
        }
        for(auto&it:mp2){
            char ch=it.first;
            int ct=it.second;
            if(mp.find(ch)==mp.end() || mp[ch]<ct)return 0; 
            else ans=min(ans,mp[ch]/ct);
        }
        return ans; 
    }
};