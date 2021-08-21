#include <iostream>
#include<stack>
#include<algorithm>
using namespace std;

int main()
{
   int n;cin>>n;
   stack<int> st;
   while(n--){
       int a;cin>>a;
       if (a==1){
           int id;cin>>id;
           st.push(id);
       }
       else if(a==2){
           if(st.size()>0){
               st.pop();

           }


       }
       else{
           if (st.size()>0){
               cout<<st.top()<<endl;

           }

       }

   }


   return 0;
}
