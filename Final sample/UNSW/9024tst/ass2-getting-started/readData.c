// Read data from file
// Written by Ran Bai Jan 2019

#include <stdio.h>
#include "stdlib.h"
#include "readData.h"
#include "DLListStr.h"
#include "LoadDataSec.h"

#define buff_size 1000

//Create a set (list) of urls to process by reading data from file “collection.txt
DLListStr GetCollection(){
    char buff[buff_size];
    FILE *fp = fopen("./collection.txt", "r");

    assert(fp != NULL);

    DLListStr L = newDLListStr();
    while (fscanf(fp, "%s", buff) != EOF){
        insertSetOrd(L, buff);
    }

    fclose(fp);
    return L;
}

// Create graph (use graph ADT in say graph.h and graph.c)
Graph GetGraph(DLListStr L){
    Graph g = newGraph(L->nitems);

    DLListNode *current = L->first;
    while (current != NULL){
        readSection1(current->value, g, L);
        current = current->next;
    }

    return g;
}

// Create Tree (use Tree ADT in say InvertedLdx.h and InvertedLdx.c)
Tree GetTree(DLListStr L){
    Tree tree = newTree();

    DLListNode *current = L->first;
    while (current != NULL){
        tree = readSection2(current->value, tree);
        current = current->next;
    }

    return tree;
}