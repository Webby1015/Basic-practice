#include <bits/stdc++.h>
using namespace std;

void fun(string a, int i){
    cout<<i<<a<<endl;
    i=i-1;
    if(i>0){
    fun(a,i);
    }
}

int main(){
    int n=10;
    fun("Hello World",n);
}
