/*
10828.
������ �����ϴ� ������ ������ ����, �Է����� �־����� ����� ó���ϴ� 
���α׷����ۼ��Ͻÿ�

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
�����̴� �߸��� ���� �θ� ������ 0�� ���ļ�, 
���� �ֱٿ� ����̰� �� ���� ����� ��Ų��.
����̴� �̷��� ��� ���� �޾� ���� �� �� ���� ���� �˰� �;� �Ѵ�. 
����̸� ��������!
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