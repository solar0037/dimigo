//test3_1315.c
//소수의 합과 개수를 구하는 프로그램

/*
#pragma warning(disable:4996)
#include <stdio.h>

int main() {
	int num, sum = 0, cnt = 0;
	printf("Enter Num: ");
	scanf("%d", &num);
	for (int i = 2; i <= num; i++) {
		int chk = 1;
		for (int j = 2; j < i; j++) {
			if (i % j == 0) {
				chk = 0;
				break;
			}
		}
		if (chk) {
			cnt++;
			sum += i;
			printf("%d ", i);
		}
	}
	printf("\n소수개수: %d개, 소수합: %d", cnt, sum);
	return 0;
}
*/