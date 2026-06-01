// Author: Ashraf
// Link: https://leetcode.com/problems/backspace-string-compare/
// Time Complexity: O(n)
// Space Complexity: O(n)
class Solution {
public:
    bool backspaceCompare(string s, string t) {
     string temp1 = "", temp2 = "";   
     for (auto it : s) {
            if (it == '#') {
                if (!temp1.empty()) {
                    temp1.pop_back();
                }
            } else {
                temp1 += it;
            }
        }
        for (auto it : t) {
            if (it == '#') {
                if (!temp2.empty()) {
                    temp2.pop_back();
                }
            } else {
                temp2 += it;
            }
        }
        return temp1 == temp2;
    }
};