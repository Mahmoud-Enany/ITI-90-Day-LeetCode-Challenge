// Author: Mohamed Saeed
// Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
// Time Complexity: O(n)
// Space Complexity: O(n)

public class Solution {
    public string RemoveDuplicates(string s) {
        Stack<char> stack = new();

        foreach(char c in s) {
            if(stack.Count() == 0) stack.Push(c);
            else if(c == stack.Peek()) {
                while(stack.Count() != 0 && stack.Peek() == c) {
                    stack.Pop();
                }
            }
            else stack.Push(c);
        }

        string result = new string(stack.Reverse().ToArray());
        return result;
    }
}
