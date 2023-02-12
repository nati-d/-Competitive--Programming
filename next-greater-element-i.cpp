class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    int n = nums2.size();
    
    unordered_map<int,int>mp;        
    stack<int>st;
    for(int i=n-1;i>=0;i--){
        if(st.empty()){
            st.push(nums2[i]);
            mp[nums2[i]]=-1;
        }
        else{
            while(!st.empty() and st.top()<nums2[i]){
                st.pop();
            }
            if(!st.empty()){
                mp[nums2[i]]=st.top();
            }
            else{
                mp[nums2[i]] = -1;
            }
            st.push(nums2[i]);
        }
    }
    vector<int>res;
    for(int i=0;i<nums1.size();i++){
        res.push_back(mp[nums1[i]]);
    }
    return res;
}
};
