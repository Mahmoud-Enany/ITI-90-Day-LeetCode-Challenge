public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        int[] arr = new int[temperatures.Length];
        Stack<int> stack = new Stack<int>();

        for (int i = 0; i < temperatures.Length; i++)
        {
            while (stack.Count>0 && temperatures[i]>temperatures[stack.Peek()])
            {
                int index = stack.Pop();
                arr[index] = i - index;
            }
            stack.Push(i);
        }
        return arr;
    }
}
