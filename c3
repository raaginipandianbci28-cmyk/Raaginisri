#include <stdio.h>

int main() {
    int n;
    int sum = 0;
    int current_element;

    // Read the number of elements
    if (scanf("%d", &n) != 1) {
        return 0;
    }

    // Read each element and add it to the sum
    for (int i = 0; i < n; i++) {
        scanf("%d", &current_element);
        sum += current_element;
    }

    // Print the final sum
    printf("%d\n", sum);

    return 0;
}
