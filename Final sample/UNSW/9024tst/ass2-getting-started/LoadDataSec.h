// Interface - Load data from url**.txt (Section-1 & Section-2)
// Written by Ran Bai

#ifndef LOADDATASEC_H
#define LOADDATASEC_H

#include <stdio.h>
#include "InvertedIdx.h"

// read Section1 from URL**.txt, in order to build graph
void readSection1(char *urlname, Graph g, DLListStr L);

// read Section2 from URL**.txt in order to create "inverted index"
Tree readSection2(char *filename, Tree tree);

#endif // !LOADDATASEC_H