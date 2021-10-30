#include <iostream>

using namespace std;

int main()
{

  int calories[4];
  int value=0;
  for(int i=0;i<4;i++){
    cin>>calories[i];
  }

  string squares;cin>>squares;
  for(int i=0;i<squares.size();i++){
    int num=squares[i]-48;
    value+=calories[num-1];
  }
  cout<<value;
    return 0;
}

