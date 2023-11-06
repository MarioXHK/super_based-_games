#include <stack>
#include <iostream>
using namespace std;
string Laundry[10];
int top = -1;
void push(string clothing) {
    if (top >= 9)
        cout << "stack is full\n";
    else {
        top++;
        Laundry[top] = clothing;
    }
}

void pop() {
    if (top <= -1)
        cout << "stack is empty\n";
    else {
        cout << "The popped element is " << Laundry[top] << endl;
        top--;
    }
}

void display() {
    if (top >= 0) {
        cout << "Stack elements are: ";
        for (int i = top; i >= 0; i--)
            cout << Laundry[i] << ", ";
        cout << endl;
    }
    else
        cout << "Stack is empty.\n";
}

int size() {
    return top;
}

int main()
{
    stack <int> myStack;
    myStack.push(15);
    myStack.push(40);
    myStack.push(2);
    myStack.push(80);
    myStack.push(4);
    
    cout << "The stack's size is " << myStack.size() << "\nit's top is " << myStack.top() << "\n\nPopping the stack elements.\n";
    while (!myStack.empty())
    {
        cout << myStack.top() << ", ";
        myStack.pop();
    }
    cout << "\n\nIt's size is now " << myStack.size() << "\nNow for pancake flavores pls give some of your favorite flavors.";
    string nyan;
    stack <string> pancakes;
    while (nyan != "0") {
        cin >> nyan;
        if (nyan != "0") {
            pancakes.push(nyan);
            cout << "Anything else? If no, just type \"0\"\n";
        }
    }
    cout << "Anyways, time to do my own stack for some reason.\n";
    char choice = '8';
    while (choice != 'z') {
        cout << top << "\nChoices:\nt for toss: toss something on top of the stack\np for pop: pop the top element of the stack\nd for display: display the full stack for some reason even though normally it would only see the first element.\ns is for size: display the size of the stack.\n";
        cin >> choice;
        if (choice == 't') {
            string c;
            cout << "What to toss on top?\n";
            cin >> c;
        }
        else if (choice == 'p')
            pop();
        else if (choice == 'd')
            display();
        else if (choice == 's')
            size();
        else if (choice != 'z')
            cout << "Try again.\n";
    }
    cout << "Goodbye.\n";
}
