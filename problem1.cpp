#include<iostream>
using namespace std;

int main()
{
  int limak_wegight , bobweight, year;
  cin>> limak_wegight >>bobweight;
  
   while(limak_wegight<=bobweight)
   {
      limak_wegight=3*limak_wegight;
      bobweight =2* bobweight;
      year++;
   }
   cout<<year;
}
