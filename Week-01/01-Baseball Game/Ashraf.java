// Author: Ashraf
// Link: https://leetcode.com/problems/baseball-game/
// Time Complexity: O(n)
// Space Complexity: O(n)
class Solution {
    public int calPoints(String[] operations) {
        List<Integer> temp = new ArrayList<>();
        for (String it : operations) {
            if (it.equals("+")) {
                temp.add(temp.get(temp.size() - 1) + temp.get(temp.size() - 2));
            } else if (it.equals("D")) {
                temp.add(temp.get(temp.size() - 1) * 2);
            } else if (it.equals("C")) {
                temp.remove(temp.size() - 1);
            } else {
                temp.add(Integer.parseInt(it));
            }
        }
        int sum = 0;
        for (int it : temp) {
            sum += it;
        }
        return sum;
    }
}