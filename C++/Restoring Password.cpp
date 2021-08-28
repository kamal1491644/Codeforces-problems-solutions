#include <iostream>
#include <stack>
#include<algorithm>
#include <map>
#include<vector>
using namespace std;

int main()
{
    int counter=0;
    string n;cin>>n;
    map<string,int>mp;

    for(int i=0;i<10;i++){
        string ss;cin>>ss;
        mp[ss]=i;
    }
    counter+=10;
    for(int i=0;i<n.length();i+=10){
        string temp =  n.substr(i,counter);

        if (mp[temp]!=-1){
            cout<<mp[temp]<<"";
        }

    }







    return 0;
}
