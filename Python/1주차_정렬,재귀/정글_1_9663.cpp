// 퀸
#include <bits/stdc++.h>
using namespace std;

int* pos;
int* flag;
int* flag_L;
int* flag_R;

void showqueen(int n){
    for(int i; i <n;i++){
        cout<<pos[i];
    } 
    cout<<endl;
}

void setqueen(int n, int count,int i){
    for(int j; j<n;j++){
        pos[i] =j;
        if (i == n-1){
            showqueen(n);
        }else{
            setqueen(n,count,i+1);
        }
    }
}

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(0);
    int n;
    cin >> n;

    flag = (int*)malloc(sizeof(int)*n);
    flag_L = (int*)malloc(sizeof(int)*(2*n-1));
    flag_R = (int*)malloc(sizeof(int)*(2*n-1));
    int count = 0;
    setqueen(n,count,0);

    return 0;
}
