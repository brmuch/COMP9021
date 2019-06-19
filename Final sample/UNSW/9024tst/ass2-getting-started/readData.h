// readData.h - interface read data from file
// written by Ran Bai Jan 2019
// Last modified, Ran Bai, Jan 2019

#ifndef READDATE_H
#define READDATE_H

#include <stdio.h>
#include "readData.h"
#include "DLListStr.h"
#include "Graph.h"
#include "InvertedIdx.h"

//Create a set (list) of urls to process by reading data from file “collection.txt
DLListStr GetCollection();

//Create empty graph (use graph	ADT	in say graph.h and graph.c)
//  For each url in the above list	
//      read <url>.txt file, and update	graph by adding	a node and outgoing	links	
Graph GetGraph(DLListStr L);

// Create Tree (use Tree ADT in say InvertedLdx.h and InvertedLdx.c)
Tree GetTree(DLListStr L);

#endif