class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        if(s.size()==0) return 0;
        unordered_map<char,int> m;
        int i = 0, j = 0, ans = 1,c = 0;
        while(j<n){
            if(!m[s[j]]){
                m[s[j]]++;
                c++;
                j++;
            }
            else if(s[i]==s[j]){
                i++;
                j++;
            }
            else{
                m[s[i]] = 0;
                i++;
                c--;
            }
            ans = max(ans,c);
        }
        return ans;
    }
};
