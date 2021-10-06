#include <iostream>

using namespace std;

int main()
{
    int problems;
    cin>>problems;
    int counter = 0;
    for(int i=0;i<problems;i++){

        int Petya,Vasya,Tonya;
        cin>>Petya>>Vasya>>Tonya;

        if ((Petya+Vasya+Tonya)>=2){
            counter+=1;
        }
    }

    cout<<counter<<endl;

}
