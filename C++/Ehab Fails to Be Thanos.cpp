#include <iostream>
#include<deque>
#include<algorithm>
using namespace std;

int main()
{
    int n;
    int sumF=0;
    int sumS=0;
    cin>>n;

    int *arr=new int(2*n);

    for(int i=0;i<(2*n);i++){
        cin>>arr[i];
    }
    sort(arr,arr+(2*n));
    for (int i=0;i<(2*n);i++){
        if (i<n){
            sumF+=arr[i];
        }else{
            sumS+=arr[i];
        }

    }
    if(sumF==sumS){
        cout<<-1;
    }else{
        for(int i=0;i<(2*n);i++){
            cout<<arr[i]<<" ";
        }
    }
    return 0;
}
