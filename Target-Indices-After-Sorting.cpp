class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        vector<int> count;
        //Insertion Sort
    for (int i = 1; i < nums.size(); i++)
    {
        int temp = nums[i];
       int j = i - 1;
        while (j >= 0 && nums[j] > temp)
        {
            nums[j + 1] = nums[j];
            j = j - 1;
        }
        nums[j + 1] = temp;
    }
    //Searching for index
    for(int i=0;i<nums.size();i++){
        if(nums[i]==target){
            count.push_back(i);
        }
    }
    

    return count;
            }
        
        
    
};
