/* test_1315.c 사호준*/
/* 최대공약수와 최소공배수 구하기*/

/*
#pragma warning(disable:4996)
#include <stdio.h>

int main() {
	int a = 0;
	int b = 0;

	int num1, num2 = 0;
	int gcd, lcm = 0;

	printf("Enter Two Number: ");
	scanf("%d %d", &a, &b);
	
	num1 = a;
	num2 = b;

	int tmp = 0;

	while (num1 != num2) {
		if (num1 < num2) {
			tmp = num1;
			num1 = num2;
			num2 = tmp;
		}
		num1 = num1 - num2;
	}
	gcd = num1;
	lcm = a * b / gcd;
	printf("GCD: %d, %d", gcd, lcm);
	
	return 0;
}
*/