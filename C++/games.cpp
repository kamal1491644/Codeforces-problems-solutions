#include <iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

int main()
{


    int n;cin>>n;
    int counter=0;
    vector<int> team1vect;
    vector<int> team2vect;
    for(int i=0;i<n;i++){
        int team1,team2;cin>>team1>>team2;
        team1vect.push_back(team1);
        team2vect.push_back(team2);
    }

    for(int i=0;i<team1vect.size();i++){
       int counting = count(team2vect.begin(), team2vect.end(),team1vect[i]);
        counter+=counting;
    }

    cout<<counter;




    return 0;
}

