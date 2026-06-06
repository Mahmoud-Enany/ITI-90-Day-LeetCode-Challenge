public class MyQueue
{

    public MyQueue()
    {

    }
    Stack<int> mystack = new();
    Stack<int> outputStack = new();
    public void Push(int x)
    {
        mystack.Push(x);
    }

    public int Pop()
    {
        if (outputStack.Count == 0)
        {
            transport();
            return outputStack.Pop();
        }
        else
        {
            return outputStack.Pop();
        }
    }

    public int Peek()
    {
        if (outputStack.Count == 0)
        {
            transport();
            return outputStack.Peek();
        }
        else
        {
            return outputStack.Peek();
        }

    }

    public bool Empty()
    {
        if (outputStack.Count == 0 && mystack.Count == 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    public void transport()
    {
            while( mystack.Count > 0)
            {
                outputStack.Push(mystack.Pop());
            }
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
