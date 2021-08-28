#include <iostream>
#include <stack>
#include<algorithm>
#include <map>
#include<vector>
using namespace std;
bool cmp(pair<string, int>& a,
         pair<string, int>& b)
{
    return a.second > b.second;
}
void sort(map<string, int>& M)
{
    vector<pair<string, int> > A;
    for (auto& it : M) {
        A.push_back(it);
    }
    sort(A.begin(), A.end(), cmp);
    for (auto& it : A) {
        cout << it.first <<endl;
    }
}
int main()
{

    int n;cin>>n;
    map<string, int> mp;

    for(int i=0;i<n;i++){
        string s;cin>>s;
        mp[s]=i;
    }

    sort(mp);

    return 0;
}
