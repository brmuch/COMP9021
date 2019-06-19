// Written by Ran Bai Jan 2019
// Part A, main function file
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "readData.h"

// struct node for ranking
typedef struct RankNode{
    char value[100];
    float rankVal;
} RankNode;

extern void outByOrd(float ** PR, Graph g, DLListStr L, int length, int pos);

// Sorting basis of qsort function, in descending order
int cmp(const void *a , const void *b){
    return (((RankNode *)a)->rankVal > ((RankNode *)b)->rankVal)?-1:1; 
}

// Using the algorithm described, calculate PageRank for every url in the file collection.txt.
void PageRank(float d, float diffPR, int maxIterations){
    DLListStr L = GetCollection();
    Graph g = GetGraph(L);         
    
    int N = L->nitems;
    float diff = diffPR;
    float ** PR = malloc(N * sizeof(float *));
    assert(PR != NULL);

    for (int i = 0; i < N; i++){             // inital PR array in the begining
        PR[i] = calloc(2, sizeof(float));
        assert(PR[i] != NULL);
        PR[i][0] = 1 / (float)N;
    }
    
    // algorithm start to calculate
    int iteration = 0;
    while (iteration < maxIterations && diff >= diffPR){
        iteration ++;
        //printf("iteration: %d", iteration);

        // PR[p[i], t+1] = (1-d) / N + d * sum(PR[p[j], t] / L[p[j]])
        for (int i = 0; i < N; i ++) {
            Anp p = findPrePoint(g, i);
            float sum = 0;

            for (int j = 0; j < p->nitems; j ++) {
                sum += PR[p->array[j]][1 - iteration%2] / outDeg(g, p->array[j]);
            }

            PR[i][iteration%2] = (1 - d) / N + d * sum;   // PR[p[i]; t+1]
            free(p);
        }
        
        // diff = sum(Abs(PR[p[i], t+1] - PR[p[i], t]))
        diff = 0;
        for (int j = 0; j < N; j ++){
            diff += fabs(PR[j][0] - PR[j][1]);
        }
        //printf("diff: %.7f\n------------\n", diff);

    }
 
    // output result into file pagerankList.txt
    outByOrd(PR, g, L, N, iteration%2);

    // free allocated memory
    for (int i = 0; i < N; i ++)
        free(PR[i]);
    free(PR);
    freeGraph(g);
}

// output data to file pagerankList.txt by order
void outByOrd(float ** PR, Graph g, DLListStr L, int length, int pos){
    FILE *fp = fopen("./pagerankList.txt", "w");
    assert(fp != NULL);
    
    // initial rd
    RankNode rd[length];
    for (int i = 0; i < length; i ++) {
        rd[i].rankVal = PR[i][pos];
        strcpy(rd[i].value, idToStr(L, i));
    }

    // RankNote array sorted
    qsort(rd, length, sizeof(RankNode), cmp);

    // output to the file pagerankList.txt
    for (int i = 0; i < length; i ++){
        fprintf(fp, "%s, %d, %.7f\n", rd[i].value, outDeg(g, strToId(L, rd[i].value)), rd[i].rankVal);
    }
   
   fclose(fp);
}

// main function
int main(int argc, char const *argv[])
{
    assert(argc == 4);
    float d = atof(argv[1]), diffPR = atof(argv[2]);    // d - damping factor, diffPR - difference in PageRank sum
    int maxIterations = atoi(argv[3]);                  // maxIterations - maximum iterations 

    PageRank(d, diffPR, maxIterations);                 // page rank algorithm

    return EXIT_SUCCESS;
}
