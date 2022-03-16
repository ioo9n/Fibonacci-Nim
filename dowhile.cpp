#include<iostream>
using namespace std;
int main ()
{

int listSize = 4;
int numberProcessed = 0 , avarge; 
double sum = 0;
for (int i = 0; i < 3; i++)
{ double value;
  cin >> value;
  avarge = sum / numberProcessed;
}

cout << "Average: " << avarge << endl;
}


