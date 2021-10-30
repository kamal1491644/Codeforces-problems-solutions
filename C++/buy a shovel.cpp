#include <iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

int main()
{

    int price,burleCoin;cin>>price>>burleCoin;
    int buy=0;
    int tempPrice=price;
    while(true){
        if(tempPrice%10==0 || (tempPrice)%10==burleCoin){
            buy+=1;
            break;
        }
        buy+=1;
        tempPrice+=price;
    }
    cout<<buy;


    return 0;
}

