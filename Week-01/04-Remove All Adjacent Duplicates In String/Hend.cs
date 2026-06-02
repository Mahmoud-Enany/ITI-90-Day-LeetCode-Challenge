public class Solution {
    public string RemoveDuplicates(string s) {
        Stack<char> st=new Stack<char>();
        foreach(char item in s){
            if(st.Count>0 && st.Peek()==item) st.Pop();
            else st.Push(item);
        }
        return new string(st.Reverse().ToArray());
    }
}
