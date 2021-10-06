#include <iostream>
#include <algorithm>
using namespace std;

int main()
{

    int matrix[5][5];

    //rows
    for (int i=0;i<5;i++){
        // columns
        for(int j=0;j<5;j++){
          cin>>matrix[i][j];
        }
    }



    //rows
    for (int i=0;i<5;i++){
        // columns
        for(int j=0;j<5;j++){

            if (matrix[i][j]==1){
                int rows = abs(i-2);
                int cols = abs(j-2);
                cout<<rows+cols<<endl;
            }
        }
        cout<<endl;
    }





}
