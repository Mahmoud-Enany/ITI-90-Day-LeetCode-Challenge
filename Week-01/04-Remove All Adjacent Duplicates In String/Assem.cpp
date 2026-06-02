// Author: Assem
// Problem: Remove All Adjacent Duplicates In String
// Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
// Time: O(n) | Space: O(n)

#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    string removeDuplicates(string s)
    {
        stack<char> stack = {};

        // abbaca

        for (int i = 0; i < s.size(); i++) // a  b  b  a c a
        {
            if (stack.empty() || stack.top() != s[i])
            {
                stack.push(s[i]); // stack : c a
            }
            else if (s[i] == stack.top())
            {
                stack.pop();
            }
        }

        string result = "";

        while (!stack.empty())
        {
            result += stack.top();
            stack.pop();
        }

        reverse(result.begin(), result.end());

        return result;
    }
};

int main()
{

    Solution s;

    s.removeDuplicates("abbaca");

    return 0;
}
