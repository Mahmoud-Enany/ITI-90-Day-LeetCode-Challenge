// Author: Ashraf
// Link: https://leetcode.com/problems/implement-stack-using-queues/
// Time Complexity: 
//    push(val) -  O(1)
//    pop() -  O(1)
//    peek() -  O(1)
//    empty() -  O(1)
// Space Complexity: O(n)
class MyStack {
public:
    queue<int> q1;
    queue<int> q2;
    MyStack() {}
    void push(int val) { q1.push(val); }
    int pop() {
        while (q1.size() > 1) {
            int val = q1.front();
            q1.pop();
            q2.push(val);
        }
        int val = q1.front();
        q1.pop();
        swap(q1, q2);

        return val;
    }
    int top() {
        while (q1.size() > 1) {
            int val = q1.front();
            q1.pop();
            q2.push(val);
        }
        int val = q1.front();
        q1.pop();
        q2.push(val);

        swap(q1, q2);
        return val;
    }
    bool empty() { return q1.empty(); }
};