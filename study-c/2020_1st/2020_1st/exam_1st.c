//#pragma warning(disable: 4996)
////#include <stdio.h>
//
////int main() {
////	int a, b, c;
////	scanf("%d %d %d", &a, &b, &c);
////	
////	if (a != b && b != c) printf("3���� ���� ��� �ٸ���.");
////	else if (a == b && b == c) printf("��� ����.");
////	else if (a == b || b == c || c == a) printf("2���� ���� ����.");
////
////	return 0;
////}
//
////int main() {
////	int num;
////	printf("�л� ���� �Է��ϼ��� : ");
////	scanf("%d", &num);
////
////	int height[10];
////	for (int i = 0; i < num; i++) {
////		printf("%d�� �л��� Ű�� �Է��Ͻÿ� : ", i+1);
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
////	for (int i = 0; i < num; i++) printf("%d�� : %d\n", i+1, height[i]);
////
////	return 0;
////}
//
////#include <stdio.h>
////#include <string.h>
////
////int main() {
////	char word[10];
////	printf("�ܾ �Է��ϼ��� : ");
////	scanf("%s", word);
////	char c;
////	printf("�˻��� ���ڸ� �Է��ϼ��� : ");
////	scanf(" %c", &c);
////
////	int cnt = 0;
////	for (int i = 0; i < strlen(word); i++) {
////		if (c == word[i]) cnt++;
////	}
////
////	if (cnt == 0) printf("%c�� �����ϴ�.", c);
////	else printf("%c�� %d���Դϴ�.", c, cnt);
////
////	return 0;
////}
//
//#include <stdio.h>
//#include <string.h>
//
//int main() {
//	char word[100], result_num[100], result_char[100], result[100];
//	printf("���ڿ��� �Է��ϼ��� : ");
//	scanf("%s", word);
//
//	for (int i = 0; i < strlen(word); i++) {
//		if (word[i] >= 48 && word[i] <= 57) {}
//	}
//
//	return 0;
//}
