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
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* current = head;

        while (current != nullptr) {
            ListNode* nextNode = current->next;
            current->next = prev;
            prev = current;
            current = nextNode;
        }
        return prev;
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        if (!head) return nullptr;
        ListNode* newHead = reverseList(head);
        ListNode* current = newHead;
        

        if (n==1) {

        newHead = newHead->next;
        } else {
        for (int i=1; i<n-1; i++) {
                    current = current->next; 
                }

                current->next = current->next->next;
        }


        return reverseList(newHead);
    }
};
