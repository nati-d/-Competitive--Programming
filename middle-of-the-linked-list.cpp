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
    ListNode* middleNode(ListNode* head) {
        // creating 2 pointers
        struct ListNode *p, *q;

        // initial position of p and q
        p = q = head;

        // p moves 1 node along the list and q moves 2 nodes along the list
        // when q reaches the end of the list, p points to the middle
        while(q->next){
            p = p->next;
            if(q->next->next) q = q->next->next;
            else q = q->next;
        }
        return p;
    }
};
