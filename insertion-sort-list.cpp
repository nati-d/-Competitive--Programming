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
    ListNode* insertionSortList(ListNode* head) {
        ListNode *dummy = new ListNode(-500000), *node;
        dummy->next = head;
        node = dummy;
        while(head)
        {
            if(node->val > head->val)
            {
                node->next = head->next;
                ListNode *ptr = dummy;
                while(ptr->next->val <= head->val)
                    ptr = ptr->next;
                head->next = ptr->next;
                ptr->next = head;
                head = node->next;
            }
            else
            {
                node = node->next;
                head = head->next;
            }
        }
        
        return dummy->next;
        
    }
};
