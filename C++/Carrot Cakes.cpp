#include <iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

int main()
{

    int cakesNeeded,timeForCakes,numberOfCakes,timeToBuild;
    cin>>cakesNeeded>>timeForCakes>>numberOfCakes>>timeToBuild;
    int newnumbercakes=0;
    int newtimeforcakes=0;
    int newtime=0;
    while(newnumbercakes<cakesNeeded){

        newtime = timeForCakes+timeToBuild;

        newnumbercakes+=numberOfCakes;

        newtimeforcakes+=timeForCakes;



    }

    if(newtime>=newtimeforcakes){
        cout<<"NO"<<endl;
    }else{
        cout<<"YES"<<endl;
    }

    return 0;
}

