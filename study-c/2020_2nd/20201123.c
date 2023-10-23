/*
숫자 4개 중 소수가 아닌 수를 반환하는 프로그램을 작성하라.
예를 들어, [5, 9, 7, 10]이라는 수가 주어지게 되면
9, 10은 결과값이 반환되도록 한다.
만약 주어진 값이 전체가 소수라면 전체 소수이다. 라고 출력한다.
*/

#include <stdio.h>


int isPrime(int);
void checkAll(int*);


int main() {
    int arr[4];
    for (int i=0; i<4; i++) {
        scanf("%d", &arr[i]);
    }

    // int result[4] = checkAll(arr);
    // int* result = checkAll(arr);
    checkAll(arr);
    // for (int i=0; i<4; i++) {
    //     printf("%d ", result[i]);
    // }

    return 0;
}

int isPrime(int n) {
    if (n == 1) {
        return 0;
    }
    for (int i = 2; i < n; i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

void checkAll(int* arr) {
    int result[5];
    int cnt = 0;

    for (int i=0; i<4; i++) {
        if (!isPrime(arr[i])) {
            printf("%d is not prime.\n", arr[i]);
            result[cnt] = arr[i];
            cnt++;
        }
    }
    if (cnt == 0) {
        printf("모든 수가 소수입니다.");
    }
}
