class Solution {
public:
    string reverseParentheses(string s) {
        stack<int>s1;
        string ans="";
        for (int i=0;i<s.size();i++)
        {
            if(s[i]=='(') s1.push(i);
            else if (s[i]==')')
            {
                int x=s1.top()+1;
                int y=i;
                reverse(s.begin()+x,s.begin()+y);
                s1.pop();
            }
        }
        for (int i=0;i<s.size();i++)
        {
            if(s[i]=='(' || s[i]==')')
            {
                continue;
            }
            else ans.push_back(s[i]);
        }
        
        return ans;
    }
};
