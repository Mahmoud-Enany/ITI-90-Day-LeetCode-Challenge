// Author: Assem
// Problem:  Implement Queue using Stacks
// Link: https://leetcode.com/problems/implement-queue-using-stacks/description/
// Time: O(n) | Space: O(n)

#include <bits/stdc++.h>
using namespace std;

class MyQueue
{
public:
    stack<int> inStack;
    stack<int> outStack;
    void push(int x)
    {
        inStack.push(x);
    }

    int pop()
    {
        if (outStack.empty())
        {
            while (!inStack.empty())
            {
                outStack.push(inStack.top());
                inStack.pop();
            }
        }

        int x = outStack.top();
        outStack.pop();

        return x;
    }

    int peek()
    {
        if (outStack.empty())
        {
            while (!inStack.empty())
            {
                outStack.push(inStack.top());
                inStack.pop();
            }
        }
        return outStack.top();
    }

    bool empty()
    {
        return inStack.empty() && outStack.empty();
    }
};

int main()
{
    MyQueue *obj = new MyQueue();
    obj->push(10);
    int param_2 = obj->pop();
    int param_3 = obj->peek();
    bool param_4 = obj->empty();

    return 0;
}
