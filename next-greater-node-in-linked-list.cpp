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
    vector<int> nextLargerNodes(ListNode* head) {
        vector<int> v;
        ListNode* temp=head;
        while(temp){
            ListNode* temp1=temp->next;
            int flag=0;
            while(temp1){
                if(temp1->val>temp->val){
                    v.push_back(temp1->val);
                    flag=1;
                    break;
                }
                temp1=temp1->next;
            }
            if(flag==0){
                v.push_back(0);
            }
            temp= temp->next;
        }
        return v;
    }
};
