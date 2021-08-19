#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    string word;
    cin>>word;
    vector<int> vect;
    int counter=0;
    word+='A';
    for(int i=0;i<word.length();i++){
        if (word[i]=='A' || word[i]=='E' ||word[i]=='I' ||word[i]=='O' ||word[i]=='U' ||word[i]=='Y'){
            counter+=1;
            vect.push_back(counter);
            counter=0;
        }else{
            counter+=1;
        }
    }


         cout << *max_element(vect.begin(), vect.end());



    return 0;
}
