/*
10093.
두 양의 정수가 주어졌을 때,
두 수 사이에 있는 정수를 모두 출력하는 프로그램을 작성하시오.
*/

#include <bits/stdc++.h>
using namespace std;
int main(void) {
	cin.tie(0);
	ios::sync_with_stdio(0);
	long long a, b;
	cin >> a >> b;
	if (a > b) swap(a, b);
	if (a != b) {
		cout << b - a - 1 << "\n";
		for (long long i = a + 1; i < b; i++) {
			cout << i << " ";
		}
	}
	else {
		cout << 0;
	}
}
