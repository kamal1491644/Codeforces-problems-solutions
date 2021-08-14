#include <iostream>
#include<deque>
#include<algorithm>
using namespace std;
// LineLand Mail Problem

int main()
{
    int n;
    cin>>n;
    int maxi;
    int mini;
    int arr[n+5];
    for (int i=0;i<n;i++){
        cin>>arr[i];
    }
    for(int i=0;i<n;i++){
        if (i!=0 && i!=n-1)
        {
            //check for min element
            int diff_prev = arr[i]-arr[i-1];
            int diff_next= arr[i+1]-arr[i];
            if (diff_prev<diff_next)
                mini=diff_prev;
            else
                mini=diff_next;
        }
        else if(i==0)
          mini=arr[i+1]-arr[i];
        else if(i==n-1)
            mini=arr[i]-arr[i-1];
        //check for the max element
        int firstElement = arr[i]-arr[0];
        int lastElement  = arr[n-1]-arr[i];
        if(firstElement>lastElement)
                maxi=firstElement;
        else
                maxi=lastElement;
        cout<<mini<<" "<<maxi<<endl;
    }
    return 0;
}
