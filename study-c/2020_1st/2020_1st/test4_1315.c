//test4_1315.c
//완전수 구하기

/*
#pragma warning(disable:4996)
#include <stdio.h>

int main() {
	int num;
	printf("Enter Num: ");
	scanf("%d", &num);
	int p[10000] = { 0 }, cnt = 0;

	for (int i = 1; i < num + 1; i++) {
		int sum = 0;
		for (int j = 1; j < i; j++) {
			if (i % j == 0) sum += j;
		}
		if (i == sum) {
			p[cnt] = i;
			cnt++;
		}
	}

	for (int i = 0; i < cnt; i++) printf("%d ", p[i]);

	printf("\n개수 %d", cnt);

	return 0;

}
*/