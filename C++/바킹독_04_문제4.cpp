/*
1406.
�ʱ⿡ �����⿡ �ԷµǾ� �ִ� ���ڿ��� �־�����, 
�� ���� �Է��� ��ɾ ���ʷ� �־����� ��, 
��� ��ɾ �����ϰ� �� �� �����⿡ �ԷµǾ� �ִ� ���ڿ��� ���ϴ� ���α׷��� �ۼ��Ͻÿ�. 
��, ��ɾ ����Ǳ� ���� Ŀ���� ������ �� �ڿ� ��ġ�ϰ� �ִٰ� �Ѵ�.
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
Ű�ΰŴ� ����ڰ� Ű���带 ���� ����� ��� ����Ѵ�.
����, �����̰� ��й�ȣ�� �Է��� ��, ȭ��ǥ�� �齺���̽��� �Է��ص� ��Ȯ�� ��й�ȣ�� �˾Ƴ� �� �ִ�.
�����̰� ��й�ȣ â���� �Է��� Ű�� �־����� ��, �������� ��й�ȣ�� �˾Ƴ��� ���α׷��� �ۼ��Ͻÿ�.
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
N�� K�� �־����� (N, K)-�似Ǫ�� ������ ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
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