# Planarity

## Problem Description

A graph is called planar if it can be drawn in the plane without any crossings. In a drawing of a graph, nodes are identified with points in the plane, and edges with lines connecting the corresponding end nodes. No edge is allowed to cross another edge or node in the drawing.

Write a program that determines whether a given undirected graph is planar or not.

## Input Description

A graph is given in the following way: First, a line contains two integers $n$ and $m$, separated by a space, where $n$ denotes the number of vertices of the graph, and $m$ denotes its number of edges ($0 \le n \le 10^5$ and $0 \le m \le 3\times 10^5$).
Then follow $m$ lines, one for every edge of the graph, each containing two integers $u$ and $v$, separated by a space, meaning that the graph contains the edge $\{u, v\}$. Vertices in the graph are labelled from $0$ to $n-1$.

## Output Description
Print a line with the string ‘YES’ if the graph is planar or with the string ‘NO’ otherwise.

## Sample Input
```
7 10
4 6
6 3
2 0
4 0
1 3
1 0
1 5
4 5
2 3
2 5
```

## Sample Output
```
NO
```