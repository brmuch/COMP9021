// Graph ADT
// Adjacency Matrix Representation 
// Written by Ashesh Mahidadia, Modify by Ran Bai Jan 2019
#include "Graph.h"
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

// new a graph which have v vertices
Graph newGraph(int V) {
   assert(V >= 0);
   int i;

   Graph g = malloc(sizeof(GraphRep));
   assert(g != NULL);
   g->nV = V;
   g->nE = 0;

   // allocate memory for each row
   g->edges = malloc(V * sizeof(int *));
   assert(g->edges != NULL);
   // allocate memory for each column and initialise with 0
   for (i = 0; i < V; i++) {
      g->edges[i] = calloc(V, sizeof(int));
      assert(g->edges[i] != NULL);
   }

   return g;
}

// search set of points which point to given node
Anp findPrePoint(Graph g, int index){
    int num = 0;

    for (int i = 0; i < g->nV; i ++){            // find number of node point to given node
        if (g->edges[i][index] == 1 && i != index)
            num ++;
    }
    
    Anp p = malloc(sizeof(ArrayNode));
    p->array = malloc(num * sizeof(int));     // malloc enough space for array
    p->nitems = num;

    for (int i = 0, j = 0; i < g->nV; i ++){
        if (g->edges[i][index] == 1 && i != index){
            p->array[j] = i;
            j ++;
        }
    }

    return p;
}

// calculate out degree of the given node 
int outDeg(Graph g, int index){
    int degree = 0;
    for (int i = 0; i < g->nV; i ++){
        if (g->edges[index][i] == 1 && i != index)
            degree ++;
    }

    return degree;
}

// check if vertex is valid in a graph
bool validV(Graph g, Vertex v) {
   return (g != NULL && v >= 0 && v < g->nV);
}

// insert an edge to the given graph
void insertEdge(Graph g, Edge e) {
   assert(g != NULL && validV(g,e.v) && validV(g,e.w));

   if (!g->edges[e.v][e.w]) {  // edge e not in directed graph
      g->edges[e.v][e.w] = 1;
      g->nE++;
   }
}

// from given graph remove an edge
void removeEdge(Graph g, Edge e) {
   assert(g != NULL && validV(g,e.v) && validV(g,e.w));

   if (g->edges[e.v][e.w]) {   // edge e in directed graph
      g->edges[e.v][e.w] = 0;
      g->nE--;
   }
}

// show a graph in the screen
void showGraph(Graph g) {
    assert(g != NULL);
    int i, j;

    printf("Number of vertices: %d\n", g->nV);
    printf("Number of edges: %d\n", g->nE);
    for (i = 0; i < g->nV; i++)
       for (j = 0; j < g->nV; j++)
	  if (g->edges[i][j])
	      printf("Edge %d - %d\n", i, j);
}

// free graph
void freeGraph(Graph g) {
   assert(g != NULL);

   int i;
   for (i = 0; i < g->nV; i++)
      free(g->edges[i]);
   free(g->edges);
   free(g);
}