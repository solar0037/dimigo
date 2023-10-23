//#pragma warning(disable: 4996)
////#include <stdio.h>
//
////int main() {
////	int a, b, c;
////	scanf("%d %d %d", &a, &b, &c);
////	
////	if (a != b && b != c) printf("3개의 값이 모두 다르다.");
////	else if (a == b && b == c) printf("모두 같다.");
////	else if (a == b || b == c || c == a) printf("2개의 값이 같다.");
////
////	return 0;
////}
//
////int main() {
////	int num;
////	printf("학생 수를 입력하세요 : ");
////	scanf("%d", &num);
////
////	int height[10];
////	for (int i = 0; i < num; i++) {
////		printf("%d번 학생의 키를 입력하시오 : ", i+1);
////		scanf("%d", &height[i]);
////	}
////
////	for (int i = 0; i < num - 1; i++) {
////		for (int j = i+1; j < num; j++) {
////			if (height[i] > height[j]) {
////				int temp = height[i];
////				height[i] = height[j];
////				height[j] = temp;
////			}
////		}
////	}
////
////	for (int i = 0; i < num; i++) printf("%d번 : %d\n", i+1, height[i]);
////
////	return 0;
////}
//
////#include <stdio.h>
////#include <string.h>
////
////int main() {
////	char word[10];
////	printf("단어를 입력하세요 : ");
////	scanf("%s", word);
////	char c;
////	printf("검색할 문자를 입력하세요 : ");
////	scanf(" %c", &c);
////
////	int cnt = 0;
////	for (int i = 0; i < strlen(word); i++) {
////		if (c == word[i]) cnt++;
////	}
////
////	if (cnt == 0) printf("%c는 없습니다.", c);
////	else printf("%c는 %d개입니다.", c, cnt);
////
////	return 0;
////}
//
//#include <stdio.h>
//#include <string.h>
//
//int main() {
//	char word[100], result_num[100], result_char[100], result[100];
//	printf("문자열을 입력하세요 : ");
//	scanf("%s", word);
//
//	for (int i = 0; i < strlen(word); i++) {
//		if (word[i] >= 48 && word[i] <= 57) {}
//	}
//
//	return 0;
//}
