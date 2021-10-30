#include <iostream>
#include<vector>
#include <bits/stdc++.h>
using namespace std;

int main()
{
   vector<unsigned long long> arr;
   vector<unsigned long long>tempArr;
   for(int i=0;i<5;i++){
        int num;cin>>num;
        arr.push_back(num);
   }

   for(int j=0;j<5;j++){
    unsigned long long sum=0;
    int tempElement=arr[j];
    for(int i=0;i<5;i++){
        sum+=arr[i];

    }
    sum-=tempElement;
    tempArr.push_back(sum);
   }

    unsigned long long &mini = *min_element(tempArr.begin(),tempArr.end());
    unsigned long long &maxi = *max_element(tempArr.begin(),tempArr.end());
    cout<<mini<<" "<<maxi;


    return 0;
}

