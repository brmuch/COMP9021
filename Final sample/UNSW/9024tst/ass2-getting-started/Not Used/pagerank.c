// Written by Ran Bai Jan 2019
// Part A, main function file
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "readData.h"

extern void outByOrd(float ** PR, Graph g, DLListStr L, int length, int pos);

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

    // copy
    for (int i = 0; i < length; i ++){
        PR[i][1-pos] = PR[i][pos]; 
    }
    // Bubble sorting
    for (int i = length - 1; i > 0; i --){
        for (int j = 0; j < i; j ++){
            if (PR[j][1-pos] < PR[j+1][1-pos]){
                double temp = PR[j][1-pos];
                PR[j][1-pos] = PR[j+1][1-pos];
                PR[j+1][1-pos] = temp;
            }
        }
    }

    // output to the file pagerankList.txt
    int index;
    for (int i = 0; i < length; i ++){
        for (index = 0; PR[i][1-pos] != PR[index][pos]; index ++);
        fprintf(fp, "%s, %d, %.7f\n", idToStr(L, index), outDeg(g, index), PR[i][1-pos]);
    }
   
   fclose(fp);
}

// main function
int main(int argc, char const *argv[])
{
    assert(argc == 4);
    float d = atof(argv[1]), diffPR = atof(argv[2]);    // d - damping factor, diffPR - difference in PageRank sum
    int maxIterations = atoi(argv[3]);                  // maxIterations - maximum iterations 

    PageRank(d, diffPR, maxIterations);

    return EXIT_SUCCESS;
}
