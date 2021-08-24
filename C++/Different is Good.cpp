

    #include <iostream>
    #include <map>
    #include<algorithm>
    #include <vector>
    #include<set>
    using namespace std;
     
    int main()
    {
     
        int n;cin>>n;
     
        string s;cin>>s;
     
        set<char> st;
     
        if (n>26)
            cout<<-1<<endl;
        else{
            for(int i=0;i<s.size();i++){
                st.insert(s[i]);
            }
     
            cout<<n-st.size()<<endl;
        }
     
     
     
     
     
