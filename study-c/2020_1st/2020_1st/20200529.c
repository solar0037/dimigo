//#pragma warning(disable:4996)
//#include <stdio.h>
//
///*
//int main() {
//	int result;
//
//	result = square(5);
//	printf("%d\n", result);
//	return 0;
//}
//
//int square(int n) {
//	return n * n;
//}
//*/
//
///*
//int main() {
//	int a, b;
//	
//	printf("두 개의 정수를 입력하세요: ");
//	scanf("%d %d", &a, &b);
//	printf("두 수 중 더 큰 수는 %d입니다.\n", get_max(a, b));
//	return 0;
//}
//
//int get_max(int x, int y) {
//	if (x > y) return x;
//	else return y;
//}
//*/
//
///*
//#include <stdio.h>
//
//void f();
//
//int main() {
//	int a, b;
//	scanf("%d %d", &a, &b);
//	f(&a, &b);
//	printf("%d %d\n", a, b);
//	return 0;
//}
//
//void f(int* a, int* b) {
//	int t;
//	t = *a;
//	*a = *b;
//	*b = t;
//}
//*/
//
//#include <stdio.h>
//
//void f();
//
//int main() {
//	int A[5] = { 66, 84, 79, 93, 48 };
//	int i, j;
//	for (i = 0; i < 4; i++)
//		for (j = i + 1; j < 5; j++)
//			if (A[i] > A[j]) f(&A[i], &A[j]);
//	for (i = 0; i < 5; i++) printf("%d ", A[i]);
//}
//
//void f(int* a, int* b) {
//	int t;
//	t = *a;
//	*a = *b;
//	*b = t;
//}
