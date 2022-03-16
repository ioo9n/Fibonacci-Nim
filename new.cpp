#include<iostream>
#include <iomanip>
#include<cmath>
using namespace std;
int main ()
{
int base ;
cout<<"enter the base lenght";
cin >>base;
 for (int i = 0; i < base; i++)
 {
    
      cout << setw(base-i) << setfill(' ')<<" ";
     cout <<setw(i)<<setfill('*')<<"*";
     cout <<setw(i)<<setfill('*')<<""<<endl;
 
 }
 
}