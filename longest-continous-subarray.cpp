class Solution {
public:
    int longestSubarray(vector<int>& A, int limit) {
        deque<int> qmax;
        deque<int> qmin;
        int n=A.size();
        int j=0;
        int ans=1;
        for(int i=0;i<n;i++){
            while(!qmax.empty() &&  A[qmax.back()]<A[i]){
                qmax.pop_back();
            }
            while(!qmin.empty() &&  A[qmin.back()]>A[i]){
                qmin.pop_back();
            }
            qmax.push_back(i);
            qmin.push_back(i);
            while(abs(A[qmax.front()]-A[qmin.front()])>limit){
                if(qmax.front()<=j){
                    qmax.pop_front();
                }
                if(qmin.front()<=j){
                    qmin.pop_front();
                }
                j++;
            }
            ans=max(ans,i-j+1);
        }
        return ans;
    }
};
