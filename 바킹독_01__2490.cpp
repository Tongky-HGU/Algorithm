/*
2490.
우리나라 고유의 윷놀이는 네 개의 윷짝을 던져서 배(0)와 등(1)이 나오는 숫자를
세어 도, 개, 걸, 윷, 모를 결정한다. 네 개 윷짝을 던져서 나온 각 윷짝의 배
혹은 등 정보가 주어질 때 도(배 한 개, 등 세 개), 개(배 두 개, 등 두 개),
걸(배 세 개, 등 한 개), 윷(배 네 개), 모(등 네 개) 중
어떤 것인지를 결정하는 프로그램을 작성하라.
*/

//#include <iostream>
//#include <algorithm>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	int tmp, ans=0;
//	for (int i = 0; i < 3; i++) {
//		for (size_t j = 0; j < 4; j++) {
//			cin >> tmp;
//			if (tmp == 0) ans++;
//		}
//		if (ans == 0) cout << "E\n";
//		if (ans == 1) cout << "A\n";
//		if (ans == 2) cout << "B\n";
//		if (ans == 3) cout << "C\n";
//		if (ans == 4) cout << "D\n";
//		ans = 0;
//	}
//}