#include <iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

int main()
{

    string n;cin>>n;
    int sum;
    int counter=0;




        while(1){
            if(n.size()==1){
                break;
            }
            for(int i=0;i<n.size();i++){
                sum+=(n[i]-48);
            }

            n=to_string(sum);
            sum=0;
            counter++;
        }
        cout<<counter;











    return 0;
}

