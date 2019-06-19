// Load Data Section
// Written by Ran Bai Jan 2019

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include "DLListStr.h"
#include "Graph.h"
#include "LoadDataSec.h"

#define max_size 1000

// read Section1 from URL**.txt, in order to build graph
void readSection1(char *urlname, Graph g, DLListStr L){

/*
   let's say urlname is "url31"
   Open "url31.txt"
   read Section-1 
	(How?, a simple approach ... 
	 skip lines until first two tokens are "#start" and  "Section-1"
	 read lines (tokens) and add the required links in graph g
	 stop reading when first two tokens are "#end" and  "Section-1"
	)
*/
    char str[max_size] = "./";
    FILE *fp = fopen(strcat(strcat(str, urlname), ".txt"), "r");
    int tok = 0, src = strToId(L, urlname), dest;
    assert(src != -1);
    char buff[max_size];

    assert(fp != NULL);
    
    while (fscanf(fp, "%s", buff) != EOF && tok < 2){
        if (strcmp(buff, "Section-1") == 0)
            tok ++;
       
        if (tok >0 && strcmp(buff, "Section-1") != 0 && strToId(L, buff) != -1){
            dest = strToId(L, buff);
            g->edges[src][dest] = 1;
            g->nE ++;
        }
        
    }
    
    fclose(fp);
}


// read Section2 from URL**.txt in order to create "inverted index"
Tree readSection2(char *filename, Tree tree){

/*
   let's say filename is "url31.txt"
   Open "url31.txt"
   read Section-2 
	(How?, a simple approach ... 
	 skip lines until first two tokens are "#start" and  "Section-2"
	 read lines (tokens) and add  words (normalised) in inverted index ADT idx
	 stop reading when first two tokens are "#end" and  "Section-2"
	)
*/
    char str[max_size] = "./";
    FILE *fp = fopen(strcat(strcat(str, filename), ".txt"), "r");
    int tok = 0;
    char buff[max_size];
    char ban_ch[] = {',', '?', '.', ';'};

    assert(fp != NULL);

    while (fscanf(fp, "%s", buff) != EOF && tok < 2){
        if (strcmp(buff, "#start") == 0 || strcmp(buff, "#end") == 0){
            fscanf(fp, "%s", buff);
            if (strcmp(buff, "Section-2") == 0){
                tok ++;
                continue;
            }
        }
        
        if (tok > 0){          
            // judge and deal with buff 
            // 1. remove the following punctuation marks, if they appear at the end of a word:
            //      '.' (dot), ',' (comma), ';' (semicolon), ? (question mark)
            for (int i = 0; i < 4; i ++){
                if (buff[strlen(buff) - 1] == ban_ch[i]){
                    buff[strlen(buff) - 1] = '\0';
                    break;
                }
            }
            // 2. converting all characters to lowercase
            for (int i = 0; i < strlen(buff); i ++)
                buff[i] = tolower(buff[i]);
            
            // create tree node or add list node directly
            if (!TreeSearch(tree, buff)){
                tree = TreeInsert(tree, buff);
            }
            
            insertSetOrd(FindTreeNode(tree, buff)->list, filename); 
        }
    }

    fclose(fp);
    return tree;
}


