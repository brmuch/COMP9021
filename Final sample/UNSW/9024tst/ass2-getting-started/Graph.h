// Graph.h - Interface to Graph ADT
// Written by Ashesh Mahidadia, Modify by Ran Bai Jan 2019
// Adjacency Matrix Representation

#ifndef GRAPH_H
#define GRAPH_H

#include "Graph.h"
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct GraphRep {
   int  **edges;   // adjacency matrix
   int    nV;      // #vertices
   int    nE;      // #edges
} GraphRep;

typedef struct GraphRep *Graph;

// vertices are ints
typedef int Vertex;

// edges are pairs of vertices (end-points) v->w
typedef struct Edge {
   Vertex v;
   Vertex w;
} Edge;

typedef struct ArrayNode {
    int *array;
    int nitems;
} ArrayNode;

typedef ArrayNode * Anp;

// new a graph which have v vertices
Graph newGraph(int);

// insert an edge to the given graph
void  insertEdge(Graph, Edge);

// from given graph remove an edge
void  removeEdge(Graph, Edge);

// show given graph in the screen
void  showGraph(Graph);

// free given graph
void  freeGraph(Graph);

// search set of points which point to given node
Anp findPrePoint(Graph, int);

// calculate out degree of the given node 
int outDeg(Graph, int);

#endif