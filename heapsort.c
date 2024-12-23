#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to swap two elements
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to heapify a subtree rooted at index
void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        swap(&arr[i], &arr[largest]);
        heapify(arr, n, largest);
    }
}

// Function to implement Heapsort
void heapsort(int arr[], int n) {
    // Build a max heap
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // Extract elements one by one
    for (int i = n - 1; i >= 0; i--) {
        swap(&arr[0], &arr[i]);
        heapify(arr, i, 0);
    }
}

// Function to generate a random array
void generateRandomArray(int arr[], int n) {
    srand(time(NULL));
    for (int i = 0; i < n; i++)
        arr[i] = rand() % 100;
}

// Function to generate a sorted array
void generateSortedArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        arr[i] = i;
}

// Function to generate a reverse sorted array
void generateReverseSortedArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        arr[i] = n - i - 1;
}

int main() {
    int n;
    printf("Enter the size of the array: ");
    scanf("%d", &n);

    int *arr = (int *)malloc(n * sizeof(int));

    // Normal sorting
    printf("Normal sorting:\n");
    generateRandomArray(arr, n);
    clock_t start = clock();
    heapsort(arr, n);
    clock_t end = clock();
    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Time taken by Heapsort: %f seconds\n", time_taken);

    // Sorting a sorted array
    printf("\nSorting a sorted array:\n");
    generateSortedArray(arr, n);
    start = clock();
    heapsort(arr, n);
    end = clock();
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Time taken by Heapsort: %f seconds\n", time_taken);

    // Sorting a reverse sorted array
    printf("\nSorting a reverse sorted array:\n");
    generateReverseSortedArray(arr, n);
    start = clock();
    heapsort(arr, n);
    end = clock();
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Time taken by Heapsort: %f seconds\n", time_taken);

    // Time complexity analysis
    printf("\nTime complexity analysis:\n");
    printf("Best case (sorted array): O(n log n)\n");
    printf("Worst case (reverse sorted array): O(n log n)\n");
    printf("Average case (random array): O(n log n)\n");

    free(arr);
    return 0;
}