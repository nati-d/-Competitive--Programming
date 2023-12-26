class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int>res;
        int arr[3]={0,0,0};

        for(int i=0;i<nums.size(); i++){
            arr[nums[i]]++;
        }

        for(int i=0; i<3;i++){
            while(arr[i]>0){
                res.push_back(i);
                arr[i]--;
            }


        }

        nums=res;
        
        
    }
};