        public class Solution
        {
            public int CalPoints(string[] operations)
            {
                Stack<int> stack = new();
                int result = 0;
                int number = 0;
                foreach(var op in operations)
                {
                    if (op == "+")
                    {
                        int first = stack.Pop();
                        int second = stack.Peek();
                        stack.Push(first);
                        stack.Push(first + second);
                        result += (first + second);
                    }
                    else if (op == "C")
                    {
                        result -= stack.Pop();
                        //stack.Pop();
                    }
                    else if (op == "D")
                    {
                        number = stack.Peek() * 2;
                        result += number;
                        stack.Push(number);

                    }

                    else
                    {
                        number = int.Parse(op);
                        stack.Push(number);
                        result += number;
                    }
                }

                return result;
            }
        }
