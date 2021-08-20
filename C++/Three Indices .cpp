#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;
const int N = 1e5;
int main()
{
    int t,n,arr[N];
    cin>>t;

    while(t--){
        vector<int> vect;
        bool flag= false;
        int start=0;

        cin>>n;
        for(int i=0;i<n;i++){
            cin>>arr[i];
        }

        for(int i=0;i<n-1;i++){
            if (start!=0){
                if(arr[i]>start && arr[i]>arr[i+1]){
                    vect.push_back(i+1);
                    vect.push_back(i+2);
                    flag=true;
                    break;
                }
            }else{
                if (arr[i]>=arr[i+1])
                    continue;
                else
                {
                    start=arr[i];
                    vect.push_back(i+1);

                }
            }



        }

        if (flag){
            cout<<"YES"<<endl;
            for(int i=0;i<vect.size();i++){
                cout<<vect[i]<<" ";
            }
        }else
            cout<<"NO"<<endl;
        vect.clear();



    }
    return 0;
}
