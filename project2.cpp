#include<iostream>
using namespace std;

int main ()
{
     int n,choose;
     cin>>n;
     for(int i=0;i<n;i++)
     {
     int x,y,z;
     cin>>x>>y>>z;
     choose+=(x+y+z>=2);
}
   cout<<choose;



}