public class Solution {
    public bool BackspaceCompare(string s, string t) {
        List<char> s1=new List<char>();
        List<char> t1=new List<char>();

        for(int i=0;i<s.Length;i++){
            if(s[i]=='#') {
                if(s1.Count > 0)
                    s1.RemoveAt(s1.Count - 1);
            }
           
            else s1.Add(s[i]);
        }
        for(int i=0;i<t.Length;i++){
            if(t[i]=='#'){
                if(t1.Count > 0)
                    t1.RemoveAt(t1.Count - 1);
            } 
            else t1.Add(t[i]);
        }
         return s1.SequenceEqual(t1);
    }
}
