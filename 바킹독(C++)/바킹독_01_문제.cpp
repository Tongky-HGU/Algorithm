///*
//1000. 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
//*/
//
//#include <iostream>
//int A, B;
//int main(void) {
//	std::cin >> A >> B;
//	std::cout << A + B;
//}
//
///*
//2557. Hello World!를 출력하시오.
//*/
//
//#include <iostream>
//int main(void) {
//	std::cin.tie(0);
//	std::ios::sync_with_stdio(0);
//
//	std::cout << "Hello World!";
//}

///*
//10171. 아래 예제와 같이 고양이를 출력하시오.
//*/
//#include <iostream>
//int main(void) {
//	std::cin.tie(0);
//	std::ios::sync_with_stdio(0);
//	std::cout << "\\    /\\\n"<<" )  ( ')\n"<<"(  /  )\n"<<" \\(__)|" ;
//}

/*
108696. 두 자연수 A와 B가 주어진다. 
이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
*/
//#include <iostream>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	int A, B;
//	cin >> A >> B;
//	cout << A + B << "\n";
//	cout << A - B << "\n";
//	cout << A * B << "\n";
//	cout << A / B << "\n";
//	cout << A % B << "\n";
//}

/*
9498. 시험 점수를 입력받아 
90 ~ 100점은 A, 80 ~ 89점은 B,
70 ~ 79점은 C, 60 ~ 69점은 D,
나머지 점수는 F를 출력하는 프로그램을 작성하시오.
*/

//#include <iostream>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	int a;
//	cin >> a;
//	if (a >= 90) cout << "A";
//	else if (a >= 80) cout << "B";
//	else if (a >= 70) cout << "C";
//	else if (a >= 60) cout << "D";
//	else cout << "F";
//}

/*
2752. 시험 점수를 입력받아
동규는 세수를 하다가 정렬이 하고싶어졌다.
숫자 세 개를 생각한 뒤에, 이를 오름차순으로 정렬하고 싶어 졌다.
숫자 세 개가 주어졌을 때, 가장 작은 수, 그 다음 수, 가장 큰 수를 출력하는 프로그램을 작성하시오.
*/

//#include <iostream>
//#include <algorithm>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	int a[3], tmp;
//	cin >> a[0] >> a[1] >> a[2];
//	sort(a, a + 3);
//	cout << a[0] <<' '<< a[1] <<' ' << a[2];
//}

/*
2753. 
연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 
1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 
하지만, 2000년은 400의 배수이기 때문에 윤년이다.
*/

//#include <iostream>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	int a;
//	cin >> a;
//	if (a % 4 == 0) {
//		if (a % 100 != 0 || a % 400 == 0) {
//			cout << '1';
//		}
//		else {
//			cout << '0';
//		}
//	}
//	else {
//		cout << "0";
//	}
//}

/*
2480.
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3*100으로 계산되어 1,300원을 받게 된다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2*1,000 으로 계산되어 12,000원을 받게 된다. 3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6*100으로 계산되어 600원을 상금으로 받게 된다.

3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.
*/

//#include <iostream>
//#include <algorithm>
//using namespace std;
//
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	int a, b, c, ans;
//	cin >> a >> b >> c;
//	if (a == b && b == c && a == c) {
//		ans = 10000 + a * 1000;
//	}
//	else if (a == b) {
//		ans = 1000 + a * 100;
//	}
//	else if (b == c) {
//		ans = 1000 + b * 100;
//	}
//	else if (c == a) {
//		ans = 1000 + c * 100;
//	}
//	else {
//		int aa[3] = { a,b,c };
//		sort(aa, aa + 3);
//		ans =  aa[2] * 100;
//	}
//	cout << ans;
//}

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

/*
2562.
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
*/

//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//    ios::sync_with_stdio(0);
//	int a, max =0, idx;
//	for (int i = 0; i < 9; i++) {
//		cin >> a;
//		if (a > max) {
//			max = a;
//			idx = i+1;
//		}
//	}
//	cout << max << "\n" << idx;
//}

/*
2576.
7개의 자연수가 주어질 때, 이들 중 홀수인 자연수들을 모두 골라 그 합을 구하고, 
고른 홀수들 중 최솟값을 찾는 프로그램을 작성하시오.
예를 들어, 7개의 자연수 12, 77, 38, 41, 53, 92, 85가 주어지면 
이들 중 홀수는 77, 41, 53, 85이므로 그 합은
77 + 41 + 53 + 85 = 256이 되고,
41 < 53 < 77 < 85
이므로 홀수들 중 최솟값은 41이 된다.
*/

//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	int a, min = 1000000, sum=0;
//	for (int i = 0; i < 7; i++) {
//		cin >> a;
//		if (a % 2 == 1) {
//			if (a < min) {
//				min = a;
//			}
//			sum += a;
//		}
//	}
//	if (sum == 0) cout << "-1";
//	else cout << sum << "\n" << min;
//}

/*
2587.
어떤 수들이 있을 때, 
그 수들을 대표하는 값으로 가장 흔하게 쓰이는 것은 평균이다. 
평균은 주어진 모든 수의 합을 수의 개수로 나눈 것이다. 
예를 들어 10, 40, 30, 60, 30의 평균은
가 된다.

평균 이외의 또 다른 대표값으로 중앙값이라는 것이 있다. 
중앙값은 주어진 수를 크기 순서대로 늘어 놓았을 때 가장 중앙에 놓인 값이다. 
예를 들어 10, 40, 30, 60, 30의 경우, 크기 순서대로 늘어 놓으면

10 30 30 40 60
이 되고 따라서 중앙값은 30 이 된다.
다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성하시오.
*/

//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	int a[5], sum =0;
//	for (int i = 0; i < 5; i++){
//		cin >> a[i];
//		sum += a[i];
//	}
//	sort(a, a + 5);
//	cout << sum / 5 << "\n" << a[2];
//}

/*
2309.
왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 
일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 
뛰어난 수학적 직관력을 가지고 있던 백설공주는,
다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.
*/

//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	int a[9],sum = 0, b,c;
//	for (int i = 0; i < 9; i++) {
//		cin >> a[i];
//		sum += a[i];
//	}
//	for (int i = 0; i < 9; i++) {
//		for (int j = i + 1; j < 9; j++) {
//			if (sum - a[i] - a[j] == 100) {
//				b = a[i];
//				c = a[j];
//				break;
//			}
//		}
//	}
//	sort(a,a + 9);
//	for (int i = 0; i < 9; i++) {
//		if (a[i] != b && a[i] != c) {
//			cout << a[i] << "\n";
//		}
//	}
//}

/*
10093.
두 양의 정수가 주어졌을 때, 
두 수 사이에 있는 정수를 모두 출력하는 프로그램을 작성하시오.
*/

//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	long long a, b;
//	cin >> a >> b;
//	if (a > b) swap(a, b);
//	if (a != b) {
//		cout << b - a - 1 << "\n";
//		for (long long i = a + 1; i < b; i++) {
//			cout << i << " ";
//		}
//	}
//	else {
//		cout << 0;
//	}
//}

/*
2577.
세 개의 자연수 A, B, C가 주어질 때 A×B×C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
예를 들어 A = 150, B = 266, C = 427 이라면
A × B × C = 150 × 266 × 427 = 17037300 이 되고,
계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
*/

//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	int a, ans = 1, num[10] = { 0, };
//	for (int i = 0; i < 3; i++){
//		cin >> a;
//		ans = ans * a;
//	}
//	for (int i = 0; ans > 0; i++)
//	{
//		num[ans%10] += 1;
//		ans /= 10;
//	}
//	for (int i = 0; i < 10; i++)
//	{
//		cout << num[i] << "\n";
//	}
//}

/*
1267.
동호는 새악대로 T 통신사의 새 핸드폰 옴머나를 샀다. 새악대로 T 통신사는 동호에게 다음 두 가지 요금제 중 하나를 선택하라고 했다.

영식 요금제
민식 요금제
영식 요금제는 30초마다 10원씩 청구된다. 이 말은 만약 29초 또는 그 보다 적은 시간 통화를 했으면 10원이 청구된다.
만약 30초부터 59초 사이로 통화를 했으면 20원이 청구된다.

민식 요금제는 60초마다 15원씩 청구된다. 이 말은 만약 59초 또는 그 보다 적은 시간 통화를 했으면 15원이 청구된다. 
만약 60초부터 119초 사이로 통화를 했으면 30원이 청구된다.

동호가 저번 달에 새악대로 T 통신사를 이용할 때 통화 시간 목록이 주어지면 어느 요금제를 사용 하는 것이 저렴한지 출력하는 프로그램을 작성하시오.
*/

//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	int n, a, y=0, m=0;
//	cin >> n;
//	for (int i = 0; i < n; i++){
//		cin >> a;
//		y += a / 30 + 1;
//		m += a / 60 + 1;
//	}
//	y = y * 10;
//	m = m * 15;
//	if (y < m) cout << "Y " << y;
//	else if (y > m) cout << "M " << m;
//	else cout << "Y M " << y;
//}