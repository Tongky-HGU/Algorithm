/*
���� N���� �̷���� ���� A�� ���� X�� �־�����. 
�̶�, A���� X���� ���� ���� ��� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
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