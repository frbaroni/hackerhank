/*
Detect a cycle in a linked list. Note that the head pointer may be 'NULL' if the list is empty.

A Node is defined as: 
    struct Node {
        int data;
        struct Node* next;
    }
*/

bool has_cycle(Node* head) {
    if(head == nullptr)
        return false;
    
    Node* slow;
    Node* fast;
    slow = fast = head;
    do {
        if(fast->next == nullptr || fast->next->next == nullptr)
            return false;
        slow = slow->next;
        fast = fast->next->next;
    } while(slow != fast);
    
    
    return true;
}
