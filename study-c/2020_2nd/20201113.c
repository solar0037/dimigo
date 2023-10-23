#include <stdio.h>


int* slice(int*, int, int);

int main() {
	printf("출력까지 잘 되는데 왜 에러가 뜰까요!\n");
	printf("일단 제출합니다.\n");
	
	int arr[16];
	printf("입력하시오 : ");
	for (int i=0; i<16; i++)
		scanf("%d", &arr[i]);
	
	int* arr1 = slice(arr, 0, 8);
	int* arr2 = slice(arr, 8, 16);
	for (int i=0; i<8; i++)
		printf("%d ", arr1[i]);
	for (int i=0; i<8; i++)
		printf("%d ", arr2[i]);
	
	return 0;
}

int* slice(int* arr, int start, int end) {
	int size = end - start;
    int* res = malloc(size*sizeof(int));
	for (int i=start; i<end; i++)
		res[i-start] = arr[i];
	
	for (int i=0; i<8; i++)
		printf("%d ", res[i]);
	return res;
}
