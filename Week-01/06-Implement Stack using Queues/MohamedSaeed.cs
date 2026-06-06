// Author: Mohamed Saeed
// Link: https://leetcode.com/problems/implement-stack-using-queues/
// Time Complexity: O(n)
// Space Complexity: O(n)

public class MyStack {
    private Queue<int> _q1; // main queue
    private Queue<int> _q2; // helper queue

    public MyStack() {
        _q1 = new Queue<int>();
        _q2 = new Queue<int>();
    }
    
    public void Push(int x) {
        // Push to helper queue
        _q2.Enqueue(x);
        
        // Move everything from q1 into q2 (behind the new element)
        while (_q1.Count > 0)
            _q2.Enqueue(_q1.Dequeue());
        
        // Swap: q1 becomes the updated queue, q2 is now empty
        (_q1, _q2) = (_q2, _q1);
    }
    
    public int Pop() {
        return _q1.Dequeue();
    }
    
    public int Top() {
        return _q1.Peek();
    }
    
    public bool Empty() {
        return _q1.Count == 0;
    }
}
