public class Solution {
    public string RemoveDuplicates(string s) {
       Stack<char> stack = new Stack<char>();
        int top = 0;

        foreach (var c in s)  //abbaca
        {
            if (stack.Count > 0 &&  stack.Peek()== c)
            {
                stack.Pop();
            }
            else
            {
                stack.Push(c);
            }
        }

        return new string(stack.Reverse().ToArray());
    }
}
