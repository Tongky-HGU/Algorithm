// 스택 수열
#include <bits/stdc++.h>
using namespace std;
int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(0);
    stack<int> stack, temp, result;
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        int a;
        cin >> a;
        if (stack.empty()) {
            result.push('+');
            stack.push(a);
        } else {
            if (a < stack.top()) {
                result.push('+');
                stack.push(a);
            } else {
                while (1) {
                    result.push('-');
                    temp.push(stack.top());
                    stack.pop();
                    if (a < stack.top()) {
                        result.push('+');
                        stack.push(a);
                        while (!temp.empty()) {
                            result.push('+');
                            stack.push(stack.top());
                            temp.pop();
                        }
                    } else if (a == stack.top()) {
                        cout << "NO\n";
                        return 0;
                    }
                    if (stack.empty()) {
                        cout << "NO\n";
                        return 0;
                    }
                }
            }
        }
    }
    for (int i; i < result.size(); i++) {
        cout << result.top();
        result.pop();
    }

    return 0;
}