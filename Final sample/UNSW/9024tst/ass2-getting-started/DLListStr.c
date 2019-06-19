/*
 Implementation of doubly-linked list ADT for string values.
 Written by Ashesh Mahidadia Jan 2018, based on code writted by John Shepherd 2015.
 You may need to modify the following implementation and test it properly before using 
 in your program.
*/
// Modify by Ran Bai Jan 2019
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>
#include "DLListStr.h"

// create a new DLListNode (private function)
static DLListNode *newDLListNode(char *val)
{
	DLListNode *new;
	new = malloc(sizeof(DLListNode));
	assert(new != NULL);

        strcpy(new->value, val);  // for int, new->value = it;
	
	new->prev = new->next = NULL;
	return new;
}

// create a new empty DLListStr
DLListStr newDLListStr()
{
	struct DLListRep *L;

	L = malloc(sizeof (struct DLListRep));
	assert (L != NULL);
	L->nitems = 0;
	L->first = NULL;
	L->last = NULL;
	L->curr = NULL;
	return L;
}

/* 
   pre-reqisite: L is ordered (increasing) with no duplicates
   post-condition: val is inserted in L, L is ordered (increasing) with no duplicates
*/
void insertSetOrd(DLListStr L, char *val){
	DLListNode *new = newDLListNode(val);

    if (L->first == NULL){    // no Node in Doubly Linked list
        L->first = new;
        L->last = new;
        L->nitems ++;
        return;
    }

    DLListNode *current = L->first;
    while (current != NULL && strcmp(current->value, new->value) < 0)
        current = current->next;

    // already find the correct place insert the new node
    if (current == NULL){                    // add new node in the last place
        L->last->next = new;
        new->prev = L->last;
        L->last = L->last->next;
        L->nitems ++;
        return;
    }
    else{
        if (strcmp(current->value, new->value) == 0){          // duplicate
            return;
        }
        else{                                                   // add new node before curr
            if (current == L->first){
                new->next = current;
                current->prev = new;
                L->first = new;
            }
            else{
                new->next = current; 
                new->prev = current->prev;
                current->prev->next = new;
                current->prev = new;
            }

            L->nitems ++;
            return;
        }
    }
}

// find corresponding Index by given String
int strToId(DLListStr L, char *val){
    int index = 0;
    DLListNode *current = L->first;

    while (current != NULL){
        if (strcmp(current->value, val) == 0)
            return index;
        index ++;
        current = current->next;
    }
    
    return -1;
}

// find corresponding String by given index
char *idToStr(DLListStr L, int index){
    if (L->first == NULL || L->nitems < index + 1)
        return NULL;
    
    DLListNode *current = L->first;
    for (int i = 0; i < index; i ++)
        current = current->next;

    return current->value;
}

// display items from a DLListStr, comma separated
void showDLListStr(DLListStr L)
{
	assert(L != NULL);
	DLListNode *curr;
	int count = 0;
	for (curr = L->first; curr != NULL; curr = curr->next){
		count++;
		if(count > 1) {
			fprintf(stdout,", ");
		}
		fprintf(stdout,"%s",curr->value);
	}
	fprintf(stdout,"\n");
}


// free up all space associated with list
void freeDLListStr(DLListStr L)
{
	assert(L != NULL);
	DLListNode *curr, *prev;
	curr = L->first;
	while (curr != NULL) {
		prev = curr;
		curr = curr->next;
		free(prev);
	}
	free(L);
}


