// Author: Ashraf
// Link: https://leetcode.com/problems/next-greater-element-i/description/
// Time Complexity: O(n + m)
// Space Complexity: O(n)
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> nxt(10001, -1);
        stack<int> st;
        for(auto it : nums2) {
            while(!st.empty() && st.top() < it) {
                nxt[st.top()] = it;
                st.pop();
            }
            st.push(it);
        }
        while(!st.empty()){
             nxt[st.top()] = -1;
             st.pop();
        }
        vector<int>ans;
        for(auto it: nums1 ){
             ans.push_back(nxt[it]);
        }
        return ans;
    }
};