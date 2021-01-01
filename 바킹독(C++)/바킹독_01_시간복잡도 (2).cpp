///*
//문제1
//N 이하의 자연수 중에서 2의 배수이거나 5의 배수인 수를 모두 합한 값을
//반환하는 함수 func1(int N)을 작성하라. N은 10만 이하의 자연수이다.
//
//*/
//
//#include <stdio.h>
//
//int func1(int N) {
//	int cnt = 0;
//	for (int i = 0; i < N; i++) {
//		if (i % 3 == 0 || i % 5 == 0) {
//			cnt += i;
//		}
//	}
//	return cnt;
//}
//
///*
//문제2
//주어진 길이 N의 int 배열 arr에서 합이 100인 서로 다른 위치의 두 원소가 존재하면
//1을, 존재하지 않으면 0을 반환하는 함수 func2(int arr[], int N)을 작성하라.
//arr의 각수는 0 이상 100 이하이고 N은 1000 이하이다.
//
//*/
//
//int func2(int arr[], int N) {
//	for (int i = 0; i < N; i++) {
//		for (int j = i+1; j <N; j++) {
//			if (arr[i] + arr[j] == 100) return 1;
//		}
//	}
//	return 0;
//}
//
//
///*
//문제3
//N이 제곱수이면 1을 반환하고 제곱수가 아니면 0을 반환하는 함수를 작성하라
//N은 10억 이하의 자연수이다.
//*/
//
//int func3(int N) {
//	for (int i = 0; i < N / 2; i++) {
//		if (i*i == N) return 1;
//	}
//	return 0;
//}
//
///*
//문제4
//N이하의 수 중에서 가장 큰 2의 거듭제곱수를 반환하는 함수 func4(int N)을 작성하라
//N은 10억 이하의 자연수이다.
//*/
//
//int func4(int N) {
//	int val = 1;
//	
//	while (2 * val <= N) val *= 2;
//
//	return val;
//}
//
//
//int main(void) {
//	//1
//	printf("%d\n",func1(16));
//
//	//2
//	int a[] = { 1, 52, 48 };
//	printf("%d\n", func2(a,3));
//
//	//3
//	printf("%d\n", func3(9));
//
//	//4
//	printf("%d\n", func4(5));
//
//	return 0;
//
//}
//
