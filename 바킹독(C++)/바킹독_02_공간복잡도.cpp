/*
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 
이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
*/

#include <iostream>
using namespace std;
int a[100005],n, x;
int main(void) {
	cin.tie(0);
	ios::sync_with_stdio(0);
	cin >> n >> x;

	for (int i = 0; i < n; i++) cin >> a[i];
	for (int i = 0; i < n; i++)
		if (a[i] < x) cout << a[i] << ' ';

	return 0;
}