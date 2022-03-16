#include <iostream>
#include <iomanip>
using namespace std ;
int main()
{
  int base;
  cout<<"enter the base";
  cin >> base;
  for (int i = 1; i <=base ; i++)
  {
      cout <<setw(base-i)<<setfill('*')<<endl;

  }
  
  
  return 0;

   
     
}