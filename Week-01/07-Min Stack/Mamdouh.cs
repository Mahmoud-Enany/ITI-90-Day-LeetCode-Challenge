Author : Ahmed Mamdouh
Link : https://leetcode.com/problems/min-stack
Time : O(n), Space :O(n)


public class MinStack
 {
     Stack<int> stack;
     Stack<int> minStack;

     public MinStack()
     {
         stack = new();
         minStack = new();
     }

     public void Push(int val)
     {
         stack.Push(val);
         if(minStack.Count() != 0)
         {
             if(val <= minStack.Peek())
             {
                 minStack.Push(val);
             }
         }
         else
         {
             minStack.Push(val);
         }
     }

     public void Pop()
     {
         if(minStack.Peek() == stack.Pop())
         {
             minStack.Pop();
         }
     }

     public int Top()
     {
         return stack.Peek();
     }

     public int GetMin()
     {
         return minStack.Peek();
     }
 }
