// Author: Assem
// Problem: Baseball Game
// Link: https://leetcode.com/problems/baseball-game/
// Time: O(n) | Space: O(n)

#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int calPoints(vector<string> &operations)
    {
        int sum = 0;
        vector<int> record = {};

        for (int i = 0; i < operations.size(); i++)
        {
            if (operations[i] != "C" && operations[i] != "D" && operations[i] != "+")
            {
                record.push_back(std::stoi(operations[i]));
            }
            else if (operations[i] == "C")
            {
                record.pop_back();
            }
            else if (operations[i] == "D")
            {
                record.push_back(record[record.size() - 1] * 2);
            }
            else if (operations[i] == "+")
            {
                record.push_back(record[record.size() - 1] + record[record.size() - 2]);
            }
        }
        for (int i = 0; i < record.size(); i++)
        {
            sum += record[i];
        }
        // cout << sum << endl;
        return sum;
    }
};

int main()
{

    Solution s;

    vector<string> operations = {"5", "2", "C", "D", "+"};
    s.calPoints(operations);

    return 0;
}
