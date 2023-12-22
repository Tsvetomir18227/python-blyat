
int main() {
    int list1[15];

    // Input loop
    for (int i = 0; i < 15; i++) {
        printf("Enter number: ");
        scanf("%d", &list1[i]);
    }

    // Reverse the array
    for (int i = 0, j = 14; i < j; i++, j--) {
        // Swap elements at positions i and j
        int temp = list1[i];
        list1[i] = list1[j];
        list1[j] = temp;
    }

    // Output
    printf("Reversed array: ");
    for (int i = 0; i < 15; i++) {
        printf("%d ", list1[i]);
    }

    return 0;
}
