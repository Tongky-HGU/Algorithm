/*
4949.
하나 또는 여러줄에 걸쳐서 문자열이 주어진다. 각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다.

입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.
*/

#include <bits/stdc++.h>
using namespace std;
int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(0);

    while (1) {
        string in;
        getline(cin, in);
        if (in == ".") break;
        stack<char> stk;
        bool invalid = true;
        for (auto i : in) {
            if (i == '(' || i == '[')
                stk.push(i);
            else if (i == ')') {
                if (stk.empty() || stk.top() != '(') {
                    invalid = false;
                    break;
                } else
                    stk.pop();
            } else if (i == ']') {
                if (stk.empty() || stk.top() != '[') {
                    invalid = false;
                    break;
                } else
                    stk.pop();
            }
        }
        if (!stk.empty()) invalid = false;
        if (invalid)
            cout << "yes\n";
        else
            cout << "no\n";
    }
}
