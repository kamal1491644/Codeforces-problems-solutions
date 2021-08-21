#include <iostream>
#include <cstring>
#include<algorithm>
#include <cctype>
using namespace std;

int main()
{
    int n;cin>>n;

    while(n--)
    {
        int lower=0,upper=0;
        string s;cin>>s;
        for(int i=0;i<s.size();i++)
        {
            if (s[i] >= 'a' && s[i] <= 'z')
                lower++;
            else if(s[i] >= 'A' && s[i] <= 'Z')
                upper++;
        }
        if (upper<lower)
            cout<<upper<<endl;
        else
            cout<<lower<<endl;


    }


   return 0;
}
