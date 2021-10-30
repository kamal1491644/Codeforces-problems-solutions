#include <iostream>
#include<vector>

using namespace std;

int main()
{

   int n;cin>>n;
    int sumleft=0;
    int sumright=0;
    int tempIndex=0;
   int arr[n][n];
   for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>arr[i][j];
        }
   }

   for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        if(i==0 && j==n-1){
            tempIndex=n-1;
            sumright=arr[i][j];
            continue;
        }
        if(i==j){
            sumleft+=arr[i][j];

        }
        if((i+j)==tempIndex){
            sumright+=arr[i][j];
        }

    }
   }
   cout<<abs(sumleft-sumright)<<endl;




    return 0;
}

