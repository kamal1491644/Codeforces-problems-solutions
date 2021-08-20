#include <iostream>
#include<deque>
#include <set>
#include<algorithm>
using namespace std;
// LineLand Mail Problem

int main()
{
    int t;
    cin>>t;

    for(int i=0;i<t;i++){
        bool flag=1;
       int firstIndex=-1;
       int lastIndex=-1;
        int temp=0;
        int n;
        cin>>n;

        int a[n];
        int b[n];

        for(int j=0;j<n;j++){
            cin>>a[j];
        }

        for(int j=0;j<n;j++){
            cin>>b[j];
        }

        // compare the difference between the two arrays
        // found first index
        for(int i=0;i<n;i++){
            if (a[i]>b[i]){
               flag=0;
            }
            if (a[i]!=b[i]){
                temp=a[i]-b[i];
                firstIndex=i;
                break;
            }
        }


        // found last index

        for(int i=0;i<n;i++){
            if (a[i]!=b[i]){
                temp=a[i]-b[i];
                lastIndex=i;
            }
        }

        // if first is -1
        if (firstIndex==-1){
            cout<<"YES"<<endl;
        }else{
            set<int>st;
            for(int i=firstIndex;i<=lastIndex;i++){
                int diff=a[i]-b[i];
                st.insert(diff);
            }

            if (!flag)
                cout<<"NO"<<endl;
            else{
                if (st.size()==1){
                    cout<<"YES"<<endl;
                }else
                    cout<<"NO"<<endl;

            }


        }




    }
    return 0;
}
