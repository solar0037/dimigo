/*
#include <stdio.h>

int main() {
    int a[4][2], s, i, j;
    for(i=0; i<4; i++) {
        printf("%d�� �л��� ����, ���α׷��� ������ �Է��Ͻÿ�.:", i+1);
        for(j=0; j<2; j++) scanf("%d", &a[i][j]);
    }
    for(i=0; i<4; i++) {
        s = 0;
        printf("%d�� �л� ����: ", i+1);
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
        printf("%d�� %d����", y, x);
        if(data[i] == 1) printf("���� ���� ���� �ֽ��ϴ�.\n");
        else if(data[i] == 2) printf("�� ���� ���� �ֽ��ϴ�.\n");
        else printf("�� ���� �������� �ʽ��ϴ�.\n");
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
            printf("%d�� %d����", y + 1, x + 1);
            if (data[y][x] == 1) printf("���� ���� ���� �ֽ��ϴ�.\n");
            else if (data[y][x] == 2) printf("�� ���� ���� �ֽ��ϴ�.\n");
            else printf("�� ���� �������� �ʽ��ϴ�.\n");
        }
    }
    return 0;
}
*/
