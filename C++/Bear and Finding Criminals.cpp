#include <iostream>
#include<vector>

using namespace std;

int main()
{

    int n,a;cin>>n>>a;
    int ones=0;
    int cities[n];
    for(int i=0;i<n;i++){
        cin>>cities[i];
        ones+=cities[i];
    }

    int pointer=a-1;
    int index=1;



    while(pointer+index<n && pointer-index>=0)
    {
        if(cities[pointer+index]==1 && cities[pointer-index]==0 || cities[pointer+index]==0 && cities[pointer-index]==1){
            ones-=1;
        }
        index++;
    }
    cout<<ones;


    return 0;
}

