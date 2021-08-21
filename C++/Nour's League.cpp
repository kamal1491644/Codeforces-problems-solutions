#include <iostream>
#include<map>
#include<algorithm>
using namespace std;

int main()
{
   int n;cin>>n;
   map<string,int> mp;
   for(int i=0;i<n;i++){
       string s,y;cin>>s>>y;
       if (y=="W")
           mp[s]+=3;
       else if (y=="D")
           mp[s]+=1;
       else
           mp[s]+=0;

   }
    cout<<mp.size()<<endl;
   for(const auto& elem : mp)
   {
       std::cout << elem.first << " " << elem.second<<endl;
   }
    return 0;
}
