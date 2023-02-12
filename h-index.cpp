class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(),citations.end());
        int n=citations.size();
        int count=0;
        for(int i=n-1;i>=0;i--)
        {
            if(n-i<=citations[i])
                count++;
        }
        return count;
    }
    
};
