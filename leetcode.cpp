// add two number
// Online C++ compiler to run C++ program online
#include <iostream>

list* (list* l1 , list* l2)
{
    node* l3 = new node();
    node* t3 = l3;
    int carry;
    
    node* t1 = l1;
    node* t2 = l2;
    int sum;
    int value;
    
    while(t1 != NULL && t2 != NULL)
    {
        carry = 0;
        sum = t1->data + t2->data;
        t1 = t1->next;
        t2 = t2->next;
        value = sum % 10;
        t3->data = value + carry;
        carry = sum / 10;
        
        if(t1!= NULL || t2 != NULL)
        {
        t3->next = new node();
        t3 = t3->next;
        }
        
    }
    
    while(t1 != NULL)
    {
     sum = t1->data + carry;
        t3->data = sum%10;
        t1 = t1->next;
        carry = a/10;
        if(t1 != NULL)
        {
        t3->next = new node();
        t3 = t3->next;
        }
    }
    
       if(t2 != NULL)
    {
     sum = t2->data + carry;
        t3->data = sum%10;
        carry = b/10;
        t2 = t2->next;
        
        if(t2 != NULL)
        {
        t3->next =  new node();
        t3 = t3->next;
            t3->data = t2->data;
        }
    }
    
    if(carry>0)
    {
        t3->next = new node();
        t3 = t3->next;
        t3->data = carry;
        t3->next = NULL;
    }
    else
    {
        t3->next = NULL;
    }
    
    
    return l3

    
    
}
        
        

int main() {
    // Write C++ code here
    std::cout << "Try programiz.pro";

    return 0;
}