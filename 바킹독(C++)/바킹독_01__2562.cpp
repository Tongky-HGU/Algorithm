/*
2562.
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
*/

#include <bits/stdc++.h>
using namespace std;
int main(void) {
	cin.tie(0);
    ios::sync_with_stdio(0);
	int a, max =0, idx;
	for (int i = 0; i < 9; i++) {
		cin >> a;
		if (a > max) {
			max = a;
			idx = i+1;
		}
	}
	cout << max << "\n" << idx;
}