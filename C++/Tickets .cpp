#include <iostream>
#include <vector>
#include<queue>
#include<algorithm>
using namespace std;

int main()
{
    int n;cin>>n;
    queue<int> q;
    while(n--)
    {
        int a,b;cin>>a>>b;
        if (a==1){
            q.push(b);
        }
        else
        {
            if (q.size()>0)
            {

                if (b==q.front()){
                    cout<<"Yes"<<endl;
                }else
                    cout<<"No"<<endl;
                    q.pop();
            }

        }
    }
    return 0;
}
