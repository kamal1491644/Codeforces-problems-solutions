#include <iostream>

using namespace std;

int main()
{
    int Limak,Bob;
    cin>>Limak>>Bob;
    int counter=0;

    while(Limak<=Bob){
        Limak*=3;
        Bob*=2;
        counter+=1;
    }

    cout<<counter<<endl;
    return 0;
}
