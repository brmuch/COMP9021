#include <stdio.h>
#include <stdlib.h>
#include "BSTree.h"

int main(int argc, char **argv) {
	Tree t = newTree();
	// initial a new Tree
	t = TreeInsert(t, 10);
	t = TreeInsert(t, 5);
	t = TreeInsert(t, 3);
	t = TreeInsert(t, 1);
	t = TreeInsert(t, 12);
	t = TreeInsert(t, 11);
	t = TreeInsert(t, 7);
	
	showTree(t);
	printf("Height: %d\n", TreeHeight(t));
	printf("Nodes: %d\n", countNodes(t));
	printf("Leafs: %d\n", countLeaf(t));
	printf("Odds: %d\n", countOdds(t));
	printf("IsBalanced?: %d", isBalanced(t));
	return 0;
}