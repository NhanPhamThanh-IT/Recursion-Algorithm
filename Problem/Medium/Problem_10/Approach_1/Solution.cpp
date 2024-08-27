#include <bits/stdc++.h>
using namespace std;
 
// Function to calculate the value of nCr using recursion
 
int comb(int n,int r){
   if(n<r){
       return 0;
   }
   if(r == 0){
       return 1;
   }
   if(r == 1){
       return n;
   }
   if(n == 1){
       return 1;
   }
   return comb(n-1,r-1)+comb(n-1,r);
}
 
// Driver code
int main(){
   int n = 10,r = 5;
   cout << comb(n,r);
}