class Solution {
public:
    int maxArea(vector<int>& height) {
        int s=0,area,ans=0;
        int e=height.size()-1;
        while(s<e){
            if(height[s]<=height[e]){
                area=height[s]*(e-s);
                ans=max(ans,area);
                s++;
            }else{
                area=height[e]*(e-s);
                 ans=max(ans,area);
                e--;
            }
           
        }
        return ans;
    }
};
