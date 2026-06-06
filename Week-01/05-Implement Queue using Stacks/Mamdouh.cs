// Author: <Ahmed Mamdouh>
// Link: https://leetcode.com/problems/implement-queue-using-stacks/
// Time: O(n) | Space: O(n)


        public class MyQueue
        {
            Stack<int> firstStack;
            Stack<int> secondStack;
            private int topElement;
            private bool firstPush = true;
            public MyQueue()
            {
                firstStack = new();
                secondStack = new();
            }

            public void Push(int x)
            {
                firstStack.Push(x);
                if (firstPush)
                {
                    topElement = x;
                    firstPush = false;
                }
            }

            public int Pop()
            {
                int result;
                while (firstStack.Count != 0)
                {
                    secondStack.Push(firstStack.Pop());
                }
                result = secondStack.Pop();
                firstPush = true;
                while (secondStack.Count != 0)
                {
                    Push(secondStack.Pop());
                }
                return result;
            }

            public int Peek()
            {
                return topElement;
            }

            public bool Empty()
            {
                return firstStack.Count == 0;
            }
        }
