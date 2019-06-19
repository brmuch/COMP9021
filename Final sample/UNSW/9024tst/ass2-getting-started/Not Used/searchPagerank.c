// Written by Ran Bai, Jan 2019
// Part C Search Engine file
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include "DLListStr.h"
#include "readData.h"

#define max_size 1000

typedef struct PageNode {       // Stucture PageNode
    char name[100];             // url name
    int freq;                   // frequency
    float weight;               // pagerank
} PageNode;

// Sorting basis of qsort function, in descending order
int cmp(const void *a , const void *b){
    if (((PageNode *)a)->freq != ((PageNode *)b)->freq)
        return ((PageNode *)a)->freq > ((PageNode *)b)->freq?-1:1;
    else
        return ((PageNode *)a)->weight > ((PageNode *)b)->weight?-1:1;
}

int main(int argc, char const *argv[]){
    if (argc == 1)              // no parameters are passed in
        return 0;

    char strLine[max_size];
    char *sep;
    FILE *fp = fopen("./invertedIndex.txt", "r");    // open two files by read mode
    FILE *fp1 = fopen("./pagerankList.txt", "r");

    assert(fp != NULL);
    assert(fp1 != NULL);

    DLListStr L = GetCollection();
    const int length = L->nitems;
    PageNode pn[length];

    // Inital PageNode list
    for (int i = 0; i < length; i ++){
        strcpy(pn[i].name, idToStr(L, i));
        pn[i].freq = 0;
    }

    // Read file invertedIndex.txt In order to initial every PageNode frequency
    rewind(fp);
    while (!feof(fp)) {
        fgets(strLine, max_size, fp);         
        sep = strtok(strLine, " ");

        for (int i = 1; i < argc; i ++) {
            if (strcmp(sep, argv[i]) == 0){
                // calculate url which contain the word when find the search words
                do{
                    sep = strtok(NULL, " ");
                    if (sep != NULL)
                        pn[strToId(L, sep)].freq ++;
                }while (sep != NULL);
                break;
            }
        }
    }

    // Read file pagerankList.txt in order to initial every PageNode weight
    rewind(fp1);
    while (!feof(fp1)){
        fgets(strLine, 100, fp1);
        sep = strtok(strLine, " ,");
        int index = strToId(L, sep);

        sep = strtok(NULL, " ,");
        sep = strtok(NULL, " ,");
        if (sep != NULL)
            pn[index].weight = atof(sep);
    }

    qsort(pn, length, sizeof(PageNode), cmp);

    // print all pages with one or more search terms(at most 30)
    for (int i = 0, size = 0; i < length; i ++) {
        if (pn[i].freq > 0){
            printf("%s\n", pn[i].name);
            size ++;
        }else{
            break;
        }

        if (size >= 30)
            break;
    }

    fclose(fp);                 // close two files
    fclose(fp1);
    return 0;
}
