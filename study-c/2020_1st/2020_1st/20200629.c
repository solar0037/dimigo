//#pragma warning(disable: 4996)
///*
//#include <stdio.h>
//
//struct student {
//	int number;
//	char name[20];
//	float height;
//};
//
////int equal(struct student, struct student);
//int equal(struct student* p1, struct student* p2);
//
//int main() {
//	struct student a = { 1, "hong", 3.8 };
//	struct student b = { 2, "kim", 4.0 };
//	//if (equal(a, b) == 1) printf("같은 학생");
//	if (equal(&a, &b) == 1) printf("같은 학생");
//	else printf("다른 학생");
//	return 0;
//}
//
////int equal(struct student s1, struct student s2) {
////	if (s1.number == s2.number) return 1;
////	else return 0;
////}
//
//int equal(struct student* p1, struct student* p2) {
//	if (p1->number == p2->number) return 1;
//	else return 0;
//}
//*/
//
//#include <stdio.h>
//#include <string.h>
//
//struct student {
//	char name[10];
//	char number[100];
//};
//
//int main() {
//	struct student s[10];
//	for (int i = 0; i < 10; i++) {
//		printf("%d번의 이름과 전화번호를 입력하세요: ", i + 1);
//		scanf("%s %s", s[i].name, s[i].number);
//	}
//
//	char nm[10];
//	printf("이름을 입력하세요: ");
//	scanf("%s", nm);
//
//	for (int i=0; i<10; i++) {
//		if (strcmp(s[i].name, nm) == 0) printf("%s", s[i].number);
//	}
//
//	return 0;
//}
