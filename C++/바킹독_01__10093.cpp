/*
10093.
�� ���� ������ �־����� ��,
�� �� ���̿� �ִ� ������ ��� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
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
