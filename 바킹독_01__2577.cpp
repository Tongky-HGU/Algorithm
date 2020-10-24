/*
2577.
세 개의 자연수 A, B, C가 주어질 때 A×B×C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
예를 들어 A = 150, B = 266, C = 427 이라면
A × B × C = 150 × 266 × 427 = 17037300 이 되고,
계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
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
