/*
10828.
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 
프로그램을작성하시오

*/

//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	int n;
//	stack<int> as;
//	cin >> n;
//	for (int i = 0; i < n; i++)	{
//		string inp;
//		cin >> inp;
//		if (inp == "push") {
//			int number;
//			cin >> number;
//			as.push(number);
//		}
//		else if (inp == "pop") {
//			if (as.empty()) cout << -1<<'\n';
//			else {
//				cout << as.top() << '\n';
//				as.pop();
//			}
//		}
//		else if (inp == "size") {
//			cout << as.size() << '\n';
//		}
//		else if (inp == "empty") {
//			if (as.empty()) cout << 1 << '\n';
//			else cout << 0 << '\n';
//		}
//		else if (inp == "top") {
//			if (as.empty()) cout << -1 << '\n';
//			else cout << as.top() << '\n';
//		}
//	}
//}

/*
10773.
재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 
가장 최근에 재민이가 쓴 수를 지우게 시킨다.
재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 
재민이를 도와주자!
*/

//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	int k;
//	long long ans=0;
//	stack<int> as;
//	cin >> k;
//	while (k--) {
//		int i;
//		cin >> i;
//		if (i == 0) {
//			if (!as.empty()) as.pop();
//		}
//		else as.push(i);
//	}
//	while (as.size()) {
//		ans += as.top();
//		as.pop();
//	}
//	cout << ans;
//}