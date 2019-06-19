// Written by Ran Bai Jan 2019
// Part B main functino file, use BST ADT to implement
#include <stdio.h>
#include <stdlib.h>
#include "readData.h"
#include "InvertedIdx.h"
#include "DLListStr.h"

extern void RTOTree(Tree t, FILE * fp);

// output by ascending order
void outByOrd(Tree t){
    FILE *fp = fopen("./invertedIndex.txt", "w");

    assert(fp != NULL);

    RTOTree(t, fp);
    fclose(fp);
}

// Recursive Traversal & Output Tree structure to file invertedIndex.txt
// In-order traversal
void RTOTree(Tree t, FILE * fp){
    if (t == NULL)
        return;

    // Left
    RTOTree(t->left, fp);

    // Mid (output current value to file)
    fprintf(fp, "%s  ", t->data);
    DLListNode *curr = t->list->first;
    while (curr != NULL){
        fprintf(fp, "%s ", curr->value);
        curr = curr->next;
    }
    fprintf(fp, "\n");

    // Right
    RTOTree(t->right, fp);
}


int main(int argc, char const *argv[])
{
    // reads data from a given collection of pages in collection.txt
    DLListStr L = GetCollection();
    Tree tree = GetTree(L);
   
    // output the tree by order to file invertedIndex.txt
    outByOrd(tree);
    
    // free all allocated memory
    freeTree(tree);
    freeDLListStr(L);

    return 0;
}
