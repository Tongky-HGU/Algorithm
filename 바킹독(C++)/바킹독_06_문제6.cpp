///*
//10845.
//정수를 저장하는 큐를 구현한 다음, 
//입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오
//*/
//
//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	int n;
//	cin >> n;
//	string in;
//	queue<int> aq;
//	while (n--) {
//		cin >> in;
//		if (in == "push") {
//			int num;
//			cin >> num;
//			aq.push(num);
//		}
//		else if (in == "pop") {
//			if (!aq.empty()) {
//				cout << aq.front() <<"\n";
//				aq.pop();
//			}
//			else cout << "-1\n";
//		}
//		else if (in == "size") {
//			cout << aq.size() << "\n";
//		}
//		else if (in == "empty") {
//			cout << aq.empty() << "\n";
//		}
//		else if (in == "front") {
//			if (!aq.empty()) cout << aq.front() << "\n";
//			else cout << "-1\n";
//		}
//		else if (in == "back") {
//			if (!aq.empty()) cout << aq.back() << "\n";
//			else cout << "-1\n";
//		}
//	}
//}