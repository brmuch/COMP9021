/*
 Inverted Index ADT (partial) implementation, written by Ashesh Mahidadia Jan 2018.
 You may need to modify the following implementation and test it properly before using 
 in your program.
*/

#ifndef INVERTEDLDX_H
#define INVERTEDLDX_H

#include <stdbool.h>
#include "InvertedIdx.h"
#include "DLListStr.h"

typedef char *Item;      // item is just a key

typedef struct Node {
   struct Node *left, *right;
   char  data[100];
   DLListStr  list;	
} Node;

typedef struct Node *Tree;

Tree newNode(Item);    // create an new node
Tree newTree();        // create an empty Tree
void freeTree(Tree);   // free memory associated with Tree
void showTree(Tree);   // display a Tree (sideways)

bool TreeSearch(Tree, Item);   // check whether an item is in a Tree
Tree TreeInsert(Tree, Item);   // insert a new item into a Tree
Tree FindTreeNode(Tree, Item); // find Tree node according to given string

#endif // !INVERTEDLDX_H
