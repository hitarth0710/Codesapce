#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 100000

int compare(const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int main() {
    srand(time(0));
    int* arr = malloc(SIZE * sizeof(int));
    for(long long i = 0; i < SIZE; i++) {
        arr[i] = rand() % 10001;
    }

    clock_t start, end;
    double cpu_time_used;

    start = clock();
    qsort(arr, SIZE, sizeof(int), compare);
    end = clock();

    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("Time taken to sort 100 elements: %f\n", cpu_time_used);
    free(arr);
    return 0;
}