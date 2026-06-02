public class MyQueue {

    public int front;
    public int back;
    Queue<int> queue = new Queue<int>();

    public MyQueue()
    { 
        front = -1; back = 0;
    }

    public void Push(int x)
    {
        queue.Enqueue(x);
        front++;
    }

    public int Pop()
    {
        return queue.Dequeue();
    }

    public int Peek()
    {
        return queue.Peek();
    }

    public bool Empty()
    {
        return queue.Count == 0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Peek();
 * bool param_4 = obj.Empty();
 */
