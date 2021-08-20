#include <iostream>
#include <set>
#include<algorithm>
using namespace std;
const int size = 1e5;
int main()
{
    int t,a[size],b[size];
    cin>>t;
    while (t--)
    {
        bool flag=1;
        int n,firstIndex=-1,lastIndex=-1;
        cin>>n;
        for(int j=0;j<n;j++)
            cin>>a[j];
        for(int j=0;j<n;j++)
            cin>>b[j];
        for(int i=0;i<n;i++)
        {
            if (a[i]>b[i])
                flag=0;
            if (a[i]!=b[i])
            {
                if(firstIndex==-1)
                    firstIndex = i;
                lastIndex = i;
            }
        }
        if(firstIndex==-1)
            cout<<"YES"<<endl;
        else
        {
            set<int>st;
            for(int i=firstIndex;i<=lastIndex;i++)
            {
                int diff=a[i]-b[i];
                st.insert(diff);
            }
            if(!flag)
                cout<<"NO"<<endl;
            else
            {
                if (st.size()==1)
                    cout<<"YES"<<endl;
                else
                    cout<<"NO"<<endl;
            }
        }
    }
    return 0;
}
