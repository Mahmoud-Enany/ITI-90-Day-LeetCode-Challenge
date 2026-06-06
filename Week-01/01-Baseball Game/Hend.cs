using System.Collections.Generic;
public class Solution {
    public int CalPoints(string[] operations) {
        Stack<int> arr=new Stack<int>();
        foreach(string item in operations){
            if(item=="C"){
                arr.Pop();
            }else if(item=="D"){
                arr.Push(arr.Peek() * 2);
            }else if(item =="+"){
                int first = arr.Pop();
                int second = arr.Peek();

                arr.Push(first);
                arr.Push(first + second);
            } 
            else arr.Push(int.Parse(item)) ;   
        }
        int sum=0;
        foreach(int item in arr){
            sum+=item;
        }
        return sum;
    }
}
