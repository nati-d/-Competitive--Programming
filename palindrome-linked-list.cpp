/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* temp=head;
        int c=0;
        stack<int>st;
        while(temp){
            st.push(temp->val);
            c++;
            temp=temp->next;
        }
        c/=2;
        temp=head;
        while(c){
            if(temp->val!=st.top())
            return false;
            st.pop();
            temp=temp->next;
            c--;
        }
        return true;
    }
};
