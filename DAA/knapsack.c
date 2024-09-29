#include <stdio.h>
#include <stdlib.h>

typedef struct{
    float value;
    float weight;
}Item;

void sorting(Item items[], int n)
{
    for(int i = 0;i<(n-1);i++)
    {
        for(int j = 0;j<(n-i-1);j++)
        {
            float ratio1 = items[j].value/items[j].weight;
            float ratio2 = items[j+1].value/items[j+1].weight;
            Item temp;
            if(ratio1 < ratio2){
                temp = items[j];
                items[j] = items[j+1];
                items[j+1] = temp;
            }
            
        }
    }
}

double knapsack(Item items[], int n, int weight)
{
    sorting(items,n);

    double totalval = 0.0;
    for (int i=0;i<n;i++)
    {
        if (weight == 0){
            break;
        }
        if(items[i].weight <= weight){
            weight = weight - items[i].weight;
            totalval = totalval + items[i].value;
        }else{
            float fraction = (float)weight/items[i].weight;
            totalval = totalval + (items[i].value*fraction);
            weight = 0;
        }

    }
    return totalval;
}

int main()
{
    int n,w;
    printf("Enter the number of items: ");
    scanf("%d",&n);
    printf("Enter the capacity of knapsack: ");
    scanf("%d",&w);
    
    Item items[n];
    for(int i = 0;i<n;i++)
    {
        printf("Enter the weight of item %d: ",(i+1));
        scanf("%f",&items[i].weight);
        printf("Enter the value of item %d: ",(i+1));
        scanf("%f",&items[i].value);

    }
    double maxval = knapsack(items, n, w);
    printf("The maximum value generated in Knapsack is %.2f\n",maxval);
    return 0;
}
