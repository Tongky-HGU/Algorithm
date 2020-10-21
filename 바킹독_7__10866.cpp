/*
정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.

push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
*/

#include <bits/stdc++.h>
using namespace std;
int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(0);
    deque<int> a;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string input;
        cin >> input;
        if (input == "push_front") {
            int input_n;
            cin >> input_n;
            a.push_front(input_n);
        } else if (input == "push_back") {
            int input_n;
            cin >> input_n;
            a.push_back(input_n);
        } else if (input == "pop_front") {
            if (!a.empty()) {
                cout << a.front() << "\n";
                a.pop_front();
            } else {
                cout << "-1\n";
            }
        } else if (input == "pop_back") {
            if (!a.empty()) {
                cout << a.back() << "\n";
                a.pop_back();
            } else {
                cout << "-1\n";
            }
        } else if (input == "size") {
            if (a.empty())
                cout << "0\n";
            else
                cout << a.size() << "\n";
        } else if (input == "empty") {
            if (a.empty())
                cout << "1\n";
            else
                cout << "0\n";
        } else if (input == "front") {
            if (!a.empty()) {
                cout << a.front() << "\n";
            } else {
                cout << "-1\n";
            }
        } else if (input == "back") {
            if (!a.empty()) {
                cout << a.back() << "\n";
            } else {
                cout << "-1\n";
            }
        }
    }
    return 0;
}
