/*
1406.
초기에 편집기에 입력되어 있는 문자열이 주어지고, 
그 이후 입력한 명령어가 차례로 주어졌을 때, 
모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오. 
단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.
*/

//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	string input;
//	cin >> input;
//	list<char> l;
//	for (auto i : input) l.push_back(i);
//	auto cursor = l.end(); 
//	int q;
//	cin >> q;
//	while (q--) {
//		char op;
//		cin >> op;
//		if (op == 'P') {
//			char add;
//			cin >> add;
//			l.insert(cursor, add);
//		}
//		else if (op == 'L') {
//			if (cursor != l.begin()) cursor--;
//		}
//		else if (op == 'D') {
//			if (cursor != l.end()) cursor++;
//		}
//		else {
//			if (cursor != l.begin()) {
//				cursor--;
//				cursor = l.erase(cursor);
//			}
//		}
//	}
//	for (auto i : l) cout << i;
//}

/*
5397.
키로거는 사용자가 키보드를 누른 명령을 모두 기록한다.
따라서, 강산이가 비밀번호를 입력할 때, 화살표나 백스페이스를 입력해도 정확한 비밀번호를 알아낼 수 있다.
강산이가 비밀번호 창에서 입력한 키가 주어졌을 때, 강산이의 비밀번호를 알아내는 프로그램을 작성하시오.
*/

//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	int n;
//	cin >> n;
//	for (int i = 0; i < n; i++)	{
//		string in;
//		cin >> in;
//		list<char> al;
//		auto cursor = al.end();
//		for (auto i : in) {
//			if (i == '<') {
//				if (cursor != al.begin()) cursor--;
//			}
//			else if (i == '>') {
//				if (cursor != al.end()) cursor++;
//			}
//			else if (i == '-') {
//				if (cursor != al.begin()) {
//					cursor--;
//					cursor = al.erase(cursor);
//				}
//			}
//			else {
//				al.insert(cursor, i);
//			}
//		}
//		for (auto i : al) cout << i;
//		cout << '\n';
//	}
//}

/*
1158.
N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
*/

//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);  
//	int n, k ,val=0;
//	cin >> n >> k;
//	list<int> al,ans;
//	auto cursor = al.begin();
//	for (int i = 1; i <= n; i++) al.push_back(i);
//	cout << '<';
//	while (!al.empty()) {
//		for (int i = 1; i < k; i++) {
//			al.push_back(al.front());
//			al.pop_front();
//		}
//		cout << al.front(); al.pop_front();
//		if (al.empty()) continue;
//		cout << ", ";
//	}
//	cout << '>';
//}