/*
#include <stdio.h>

int main() {
    int a[4][2], s, i, j;
    for(i=0; i<4; i++) {
        printf("%d번 학생의 수학, 프로그래밍 성적을 입력하시오.:", i+1);
        for(j=0; j<2; j++) scanf("%d", &a[i][j]);
    }
    for(i=0; i<4; i++) {
        s = 0;
        printf("%d번 학생 점수: ", i+1);
        for(j=0; j<2; j++) s += a[i][j];
        printf("%d\n", s);
    }
    return 0;
}
*/

/*
#include <stdio.h>
int main() {
    char data[12] = {0, 0, 2, 0, 1, 1, 0, 0, 2, 1, 0, 2};
    int i, x, y;
    for(i=0; i<12; i++) {
        x = i % 4 + 1;
        y = i / 4 + 1;
        printf("%d행 %d열에", y, x);
        if(data[i] == 1) printf("검은 돌이 놓여 있습니다.\n");
        else if(data[i] == 2) printf("흰 돌이 놓여 있습니다.\n");
        else printf("는 돌이 놓여있지 않습니다.\n");
    }
    return 0;
}
*/

/*
#include <stdio.h>
int main() {
    char data[3][4] = { {0, 0, 2, 0}, {1, 1, 0, 0}, {2, 1, 0, 2} };
    
    //0 0 2 0
    //1 1 0 0
    //2 1 0 2
    
    int x, y;

    for (y = 0; y < 3; y++) {
        for (x = 0; x < 4; x++) {
            printf("%d행 %d열에", y + 1, x + 1);
            if (data[y][x] == 1) printf("검은 돌이 놓여 있습니다.\n");
            else if (data[y][x] == 2) printf("흰 돌이 놓여 있습니다.\n");
            else printf("는 돌이 놓여있지 않습니다.\n");
        }
    }
    return 0;
}
*/
