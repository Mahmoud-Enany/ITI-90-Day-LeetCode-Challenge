// Author: <Ahmed Mamdouh>
// Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string
// Time: O(n) | Space: O(n)

        public class Solution
        {
            public string RemoveDuplicates(string s)
            {

                Stack<char> stack = new();
                foreach(char c in s)
                {
                    if(stack.Count > 0 && stack.Peek() == c)
                    {
                        stack.Pop();
                    }
                    else
                    {
                        stack.Push(c);
                    }
                }
                StringBuilder sb = new();
                foreach(char c in stack)
                {
                    sb.Append(c);
                }

                for(int i = 0; i < sb.Length / 2;i++)
                {
                    char temp = sb[i] ;
                    sb[i] = sb[sb.Length - 1 - i];
                    sb[sb.Length - 1 - i] = temp;
                }

                return sb.ToString();
            }
        }
