#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>
typedef struct {
	int no;
	char name[20];
}Member;

#define MEMBER_NO 1
#define MEMBER_NAME 2

int MemberNoCmp(const Member* x, const Member* y) {
	return x->no < y->no ? -1 : x->no > y->no ? 1 : 0;
}
int MemberNameCmp(const Member* x, const Member* y) {
	return strcmp(x->name, y->name);
}
void PrintMember(const Member* x) {
	printf("%d %s", x->no, x->name);
}
void PrintLnMember(const Member* x) {
	printf("%d %s\n", x->no, x->name);
}
Member ScanMember(const char* message, int sw) {
	Member temp;
	printf("%s 하는 데이터를 입력하라\n", message);
	// if (sw & MEMBER_NO) {
		printf("번호 : ");
		scanf("%d", &temp.no);
	// }
	// if (sw & MEMBER_NAME) {
		printf("이름 :");
		scanf("%s", temp.name);
	// }
	return temp;
}

typedef struct binaryNode {

	Member data; // 회원data
	struct binaryNode* left; // 왼쪽 노드
	struct binaryNode* right; // 오른쪽 노드

}BNode;
// Node를 표현하는 구조체

BNode* Search(BNode* p, const Member* x);
BNode* Add(BNode* p, const Member* x);
int Remove(BNode** root, const Member* x);
void PrintTree(const BNode* p);
void FreeTree(BNode* p);

static BNode* AllocBNode(void) {
	return calloc(1, sizeof(BNode));
}
//Node를 생성하는 함수

static void SetBNode(BNode* n, const Member* x, const BNode* left, const BNode* right) {
	n->data = *x;
	n->left = left;
	n->right = right;
}
//Node Member의 값을 설정하는 함수

BNode* Search(BNode* p, const Member* x) {
	int cond;
	if (p == NULL)
		return NULL;
	else if ((cond = MemberNoCmp(x, &p->data)) == 0)
		return p;
	else if (cond < 0)  // 실제 값이 0보다 작은 것이 아닌, 앞과 뒤의 의미
		Search(p->left, x);
	else
		Search(p->right, x);
}
//Key 값으로 검색하는 Search 함수

BNode* Add(BNode* p, const Member* x) {
	int cond;
	if (p == NULL) {
		p = AllocBNode();
		SetBNode(p, x, NULL, NULL);
	}
	else if ((cond = MemberNoCmp(x, &p->data)) == 0)
		printf("[오류] %d는 이미 등록되어 있습니다.\n", x->no);
	else if (cond < 0)
		p->left = Add(p->left, x);
	else
		p->right = Add(p->right, x);

	return p;
}

int Remove(BNode** root, const Member* x) {
	BNode* next, * temp;
	BNode** left;
	BNode** p = root;

	while (1) {
		int cond;
		if (*p == NULL) {
			printf("[오류] %d는 등록되어있지 않습니다.\n", x->no);
			return -1;
		}
		else if ((cond = MemberNoCmp(x, &(*p)->data)) == 0)
			break;
		else if (cond < 0)
			p = &((*p)->left);
		else
			p = &((*p)->right);
	}

	if ((*p)->left == NULL)
		next = (*p)->right;
	else {
		left = &((*p)->left);
		while ((*left)->right != NULL)
			left = &(*left)->right;

		next = *left;
		*left = (*left)->left;
		next->left = (*p)->left;
		next->right = (*p)->right;
	}
	temp = *p;
	*p = next;
	free(temp);

	return 0;
}

void PrintTree(const BNode* p) {
	if (p != NULL) {
		PrintTree(p->left);
		PrintLnMember(&p->data);
		PrintTree(p->right);
	}
}

void FreeTree(BNode* p) {
	if (p != NULL) {
		FreeTree(p->left);
		FreeTree(p->right);
		free(p);
	}
}

typedef enum {
	TERMINATE, ADD, REMOVE, SEARCH, PRINT
} Menu;

Menu SelectMenu(void) {
	int ch;
	do {
		printf("(1)삽입 (2)삭제 (3)검색 (4)출력 (0)종료 : ");
		scanf("%d", &ch);
	} while (ch < TERMINATE || ch > PRINT);
	return (Menu)ch;
}

int main(void) {
	Menu menu;
	BNode* root = NULL;

	do {
		Member x;
		BNode* temp;
		switch (menu = SelectMenu()) {
		case ADD :
			x = ScanMember("삽입", MEMBER_NO | MEMBER_NAME);
			root = Add(root, &x);
			break;

		case REMOVE :
			x = ScanMember("삭제", MEMBER_NO);
			Remove(&root, &x);
			break;

		case SEARCH :
			x = ScanMember("검색", MEMBER_NO);
			if ((temp = Search(root, &x)) != NULL)
				PrintLnMember(&temp->data);
			break;

		case PRINT :
			printf("[모든 노드 출력]\n");
			PrintTree(root);
			break;
		}
	} while (menu != TERMINATE);

	FreeTree(root);

	return 0;
}
