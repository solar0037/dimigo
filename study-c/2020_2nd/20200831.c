#pragma warning(disable: 4996)
#include <stdio.h>
#include <stdlib.h>

/*
int main() {
	int* x;
	x = calloc(1, sizeof(int));
	
	if (x == NULL) printf("메모리 할당 실패.\n");
	else {
		*x = 57;
		printf("*x=%d\n", *x);
		free(x);
	}

	return 0;
}
*/

/*
int main() {
	int i;
	int* a;
	int na;

	printf("요소 개수:");
	scanf("%d", &na);
	a = calloc(na, sizeof(int));

	if (a == NULL) printf("메모리 확보 실패\n");
	else {
		printf("%d개의 정수 입력:", na);
		for (i = 0; i < na; i++) {
			printf("a[%d]:", i);
			scanf("%d", &a[i]);
		}
		printf("요소의 값 출력.\n");
		for (i = 0; i < na; i++)
			printf("a[%d]=%d\n", i, a[i]);
		free(a);
	}

	return 0;
}
*/

/*
struct student {
	int number;
	char name[20];
	double grade;
};

int main() {
	struct student list[3];
	int i;

	for (i = 0; i < 3; i++) {
		scanf("%d", &list[i].number);
		scanf("%s", &list[i].name);
		scanf("%lf", &list[i].grade);
	}

	for (i = 0; i < 3; i++) {
		printf("%s, %lf\n", list[i].name, list[i].grade);
	}

	return 0;
}
*/

struct student {
	int number;
	char name[29];
	double grade;
};

int main() {
	struct student s = { 2020, "이호선", 4.3 };
	struct student* p;

	p = &s;

	printf("%d %s %f\n", s.number, s.name, s.grade);
	printf("%d %s %f\n", (*p).number, (*p).name, (*p).grade);
	printf("%d %s %f\n", p->number, p->name, p->grade);

	return 0;
}
