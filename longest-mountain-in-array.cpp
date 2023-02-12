class Solution {
public:
    int longestMountain(vector<int>& arr) {
        int n = arr.size();
        int ans = 0;
        int flg=0,flg1=0;
        int prev=-1;
        for(int i=1;i<n;)
        {
            if(arr[i-1]<arr[i] && flg1==0)
            {
                
                flg=1;
                if(prev==-1)
                prev=i-1;
                i++;
            }
            else if(arr[i-1]<arr[i] && flg1)
            {
                flg1=0;
                flg=1;
                prev=i-1;
                i++;

            }
            else if(arr[i-1]>arr[i] && flg)
            {
                flg1=1;
                ans=max(ans,(i-prev)+1);
                i++;
            }
            else
            {
                if(flg && flg1)
                {
                    ans=max(ans,(i-1-prev));
                    flg=0;
                    flg1=0;
                    prev=-1;
                }
                else
                {
                    prev=-1;
                    flg=0;
                    flg1=0;
                }
                i++;
            }
        }
        return ans;
    }
};
