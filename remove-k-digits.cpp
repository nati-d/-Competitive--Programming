class Solution {
public:
    string removeKdigits(string num, int k) {
        stack<char> st;
        int ptr {}, len=num.length();
        if(len==k)
            return "0";
        while(ptr<len){
            while(k>0 && !st.empty() && st.top()>num[ptr]){
                k--;
                st.pop();
            }
            st.push(num[ptr++]);
        }
        while(k>0){
            st.pop();
            k--;
        }
        string ans;
        while(!st.empty()){
            ans.push_back(st.top());
            st.pop();
        }
        while(ans.length()>1 && ans.back()=='0'){
            ans.pop_back();
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
