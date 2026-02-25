// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;

struct stack
{
  int size;
  int top ;
  int *arr;
};

void ad(int value , stack *s)
{
    if(s->top == s->size - 1)
    {
        cout<<"\n stack is full";
    }
    s->top++;
    s->arr[s->top] = value;
    
}

void pop(stack *s)
{
    if(s->top == -1)
    {
        cout<<"stack is empty"; 
    }
    
    cout<<"\n"<<s->arr[s->top];
    s->top--;
}

void push_(int x , stack *s)
{
    if(s->top == s->size - 1)
    {
        cout<<"stack is full";
    }
    s->top++;
    s->arr[s->top] = x;
}

void peek(int i , stack *s)
{
    if(i <= -1)
    {
        cout<<"invalid index";
    }
    cout<<s->arr[i];
}


void display( stack *s)
{
    for(int i = 0 ; i <= s->top ; i++)
    {
        cout<<" "<<s->arr[i]<<" ";
    }
}

void top(stack *s)
{
    if(s->top == -1)
    {
        cout<<"stack is empty , so there is no top stack";
    }
    else
    {
    cout<<s->arr[s->top];
    }
}

void bottom(stack *s)
{
    if(s->top == -1)
    {
        cout<<"Stack is empty , so there is no bottom element";
    }
    else
    {
        cout<<s->arr[0];
    }
}

int main() {
    // Write C++ code here
    
    stack s;
    s.size = 100;
    s.top = -1; //index pos is -1 so there is no element in array
    s.arr = new int[s.size];
    
    int n;
    cout<<"Number of elements to insert in stack :";
    cin>>n;
    
    int value;
    for(int i = 0 ; i < n ;i++)
    {
        cin>>value;
        ad(value , &s);
    }
    
   display(&s);
   
    push_(7 , &s);
    push_(8 , &s);
    cout<<"\n";
    display(&s);
    cout<<"\n";
    peek(1 , &s);
    cout<<"\n";
    display(&s);
    cout<<"\n";
    top(&s);
    cout<<"\n";
    bottom(&s);


    return 0;
}


// implementation using linked list
// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;

struct node
{
  int data;
  node* next;
};

    node* top = NULL;

void push(int value)
{ 
    node* head = new node();
    head->data = value;
    head->next = top;
    top = head;
}

void show() 
{
    node* temp = top;
    
    while(temp != NULL)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}


int main() {
    // Write C++ code here
    push(1);
    push(2);
    push(3);
    show();

    
    

    return 0;
}// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;

struct node
{
  int data;
  node* next;
};

    node* top = NULL;

void push(int value)
{ 
    node* head = new node();
    head->data = value;
    head->next = top;
    top = head;
}

void show() 
{
    node* temp = top;
    
    while(temp != NULL)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}


int main() {
    // Write C++ code here
    push(1);
    push(2);
    push(3);
    show();

    
    

    return 0;
}