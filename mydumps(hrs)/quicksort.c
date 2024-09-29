#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void quicksort(int [], int , int);
int partition(int[], int, int);
void swaping(int[], int, int);
void reverseArray(int [] , int );

int main()
{
    int SIZE;
    printf("Enter size of array: ");
    scanf("%d",&SIZE);
    int *arr = (int*)malloc(SIZE*sizeof(int));

    for(int i = 0;i<SIZE;i++)
    {
        arr[i] = rand() % SIZE;
    }

    int p = 0;
    int r = SIZE - 1;

    clock_t start, end;
    double cpu_time;

    start = clock();

    quicksort(arr,p,r);

    end = clock();

    /*
    for(int t = 0 ;t<SIZE;t++){
        printf("%d ",arr[t]);
    }*/

    printf("\n");

    cpu_time = ((double)end - start)/CLOCKS_PER_SEC;
    printf("Time taken by QuickSort is %f.\n",cpu_time);

    clock_t start2,end2;
    double cpu_time2;

    start2 = clock();

    quicksort(arr,p,r);

    end2 = clock();

    cpu_time2 = ((double)end2 - start2)/CLOCKS_PER_SEC;
    printf("Time taken by sorted input in QuickSort is %f.\n",cpu_time2);

    
    reverseArray(arr , SIZE) ; 
    clock_t start3,end3;
    double cpu_time3;

    start3 = clock();
    quicksort(arr,p,r);
    end3 = clock();

    cpu_time3 = ((double)end3 - start3)/CLOCKS_PER_SEC;
    printf("Time taken by reverse sorted input in QuickSort is %f.\n",cpu_time3);
    

    return 0;
}

void quicksort(int n[], int p, int r)
{
    int q;
    if(p < r){
        q = partition(n,p,r);
        quicksort(n,p,q-1);
        quicksort(n,q+1,r);
    }
}

int partition(int n[], int p, int r)
{
    int x;
    x = n[r];
    int i = p - 1;
    int temp;
    for(int j = p; j <= r - 1 ;j++)
    {
        if(n[j] <= x)
        {
            i = i + 1;
            //swaping(n,i,j);
            temp = n[j];
            n[j] = n[i];
            n[i] = temp;

        }
    }
    //swaping(n,i+1,r);
    temp = n[r];
    n[r] = n[i+1] ; 
    n[i+1] = temp;
    return (i+1);
}

void swaping(int n[], int i, int j) 
{
    int temp = n[i];
    n[i] = n[j];
    n[j] = temp;
}

void reverseArray(int* arr, int size) 
{
    int start = 0;
    int end = size - 1;
    while (start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}