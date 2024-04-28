/*
#define STACK_SIZE 5
typedef int element;
element stack[STACK_SIZE];
int top = -1;

void push(element item) {
    if (top >= STACK_SIZE - 1) printf("Stack is full.\n");
    else stack[++top] = item;
}

element pop() {
    if (top == -1) printf("Empty\n");
    else return stack[top--];
}

element peek() {
    if (top == -1) printf("Stack is Empty\n");
    else return stack[top];
}
*/
