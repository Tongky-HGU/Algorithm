/*
2562.
9���� ���� �ٸ� �ڿ����� �־��� ��, �̵� �� �ִ��� ã�� �� �ִ��� �� ��° �������� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.

���� ���, ���� �ٸ� 9���� �ڿ���

3, 29, 38, 12, 57, 74, 40, 85, 61

�� �־�����, �̵� �� �ִ��� 85�̰�, �� ���� 8��° ���̴�.
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