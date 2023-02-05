class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        long i=0,j=0;
        long sum=0,ans=0;

        while(j<size(nums)){
            sum+=nums[j];
            while(nums[j]*(j-i+1)>sum+k){
                sum-=nums[i];
                i++;
            }
            if(ans<j-i+1){
                ans=j-i+1;
            }
            j++;
        }
        return ans;

    }
};
   
