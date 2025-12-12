#include <stdio.h>

int arr[] = {4, 1, 13, 7, 0, 2, 8, 11, 3}; // bisa ganti sesuai kebutuhan
int n = 9;

int bestSeq[100];
int bestLen = 0;

void dfs(int index, int seq[], int len) {
    // update lis terbaik
    if (len > bestLen) {
        bestLen = len;
        for (int i = 0; i < len; i++)
            bestSeq[i] = seq[i];
    }

    // mencoba semua angka setelah index
    for (int i = index + 1; i < n; i++) {
        if (arr[i] > arr[index]) {
            seq[len] = arr[i];
            dfs(i, seq, len + 1);
        }
    }
}

int main() {
    int seq[100];

    for (int i = 0; i < n; i++) {
        seq[0] = arr[i];
        dfs(i, seq, 1);
    }

    printf("Array: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);

    printf("\n\nLargest Monotonically Increasing Subsequence: ");
    for (int i = 0; i < bestLen; i++) {
        printf("%d ", bestSeq[i]);
    }

    printf("\nPanjang LIS = %d\n", bestLen);
    return 0;
}
