/*
2577.
�� ���� �ڿ��� A, B, C�� �־��� �� A��B��C�� ����� ����� 0���� 9���� ������ ���ڰ� �� ���� ���������� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
���� ��� A = 150, B = 266, C = 427 �̶��
A �� B �� C = 150 �� 266 �� 427 = 17037300 �� �ǰ�,
����� ��� 17037300 ���� 0�� 3��, 1�� 1��, 3�� 2��, 7�� 2�� ������.
*/

#include <bits/stdc++.h>
using namespace std;
int main(void) {
	cin.tie(0);
	ios::sync_with_stdio(0);
	int a, ans = 1, num[10] = { 0, };
	for (int i = 0; i < 3; i++){
		cin >> a;
		ans = ans * a;
	}
	for (int i = 0; ans > 0; i++)
	{
		num[ans%10] += 1;
		ans /= 10;
	}
	for (int i = 0; i < 10; i++)
	{
		cout << num[i] << "\n";
	}
}
