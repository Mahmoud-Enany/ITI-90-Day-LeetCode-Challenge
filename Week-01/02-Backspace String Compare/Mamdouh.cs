// Author: Ahmed Mamdouh
// Link: https://leetcode.com/problems/backspace-string-compare/
// Time Complexity: O(n)
// Space Complexity: O(n)


public class Solution
   {
       public bool BackspaceCompare(string s, string t)
       {
           Stack<char> stackS = new();
           Stack<char> stackT = new();

           foreach(char c in s)
           {
               if(c == '#')
               {
                   if(stackS.Count != 0)
                   {
                       stackS.Pop();
                   }
               }
               else
               {
                   stackS.Push(c);
               }
           }

           foreach (char c in t)
           {
               if (c == '#')
               {
                   if (stackT.Count != 0)
                   {
                       stackT.Pop();
                   }
               }
               else
               {
                   stackT.Push(c);
               }
           }

           if (stackS.Count == stackT.Count)
           {
               int count = stackS.Count;
               //int i = stackS.Count;
               for(int i = 0; i < count; i++)
               {
                   if (stackS.Pop() != stackT.Pop())
                       return false;
               }
           }
           else
           {
               return false;
           }
           return true;
       }
   }
