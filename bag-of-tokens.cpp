class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        sort(tokens.begin(),tokens.end());
        int n=tokens.size(),i=0,j=n-1,ans=0,res=0;
        while(i<=j)
        {
            if(power>=tokens[i])
            {
                power-=tokens[i];
                i++;
                ans++;
                res=max(res,ans);
            }
            else
            {
                if(ans>0)
                {
                    power+=tokens[j];
                    j--;
                    ans--;
                }
                else
                {
                    break;
                }
            }
        }
        return res;
    }
};
