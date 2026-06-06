// Author: Assem
// Problem:  Daily Temperatures
// Link: https://leetcode.com/problems/daily-temperatures/description/
// Time: O(n²) | Space: O(n)

#include <bits/stdc++.h>
using namespace std;

// Input: temperatures = [73,74,75,71,69,72,76,73]
// Output: [1,1,4,2,1,1,0,0]

class Solution
{
public:
    vector<int> dailyTemperatures(vector<int> &temperatures)
    {
        vector<int> days;

        for (int i = 0; i < temperatures.size(); i++)
        {
            int distance = 0;

            for (int j = i + 1; j < temperatures.size(); j++)
            {
                if (temperatures[j] > temperatures[i])
                {
                    distance = j - i;
                    break;
                }
            }

            days.push_back(distance);
        }

        return days;
    }
};
