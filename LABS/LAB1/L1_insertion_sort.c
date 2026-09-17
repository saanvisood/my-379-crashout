#include <stdio.h>
#include <stdlib.h>

#define N 10

int arr[N];

void insertionSort(int A[], int length);
void printArray(int A[], int length);

void insertionSort(int A[], int length) {
    for (int i = 1; i < length; i++) {
        int key = A[i];
        int j = i - 1;
        while (j >= 0 && A[j] > key) {
            A[j + 1] = A[j];
            j -= 1;
        }
        A[j + 1] = key;
    }
}

void printArray(int A[], int length) {
    for (int i = 0; i < length; i++) {
        printf("%d ", A[i]);
    }
    printf("\n");
}

int main(void) {
    for (int i = 0; i < N; i++) {
        arr[i] = rand() >> 10;
    }
    printf("Lab 1 - C insertion sort\n");
    printf("List before sorting: ");
    printArray(arr, N);
    insertionSort(arr, N);
    printf("List after sorting: ");
    printArray(arr, N);

    return 0;
}