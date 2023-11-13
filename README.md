## Objective:

- Starting from the file files/quadtree.txt, generate the associated QuadTree. Then, create a graphical interface using the TkQuadTree class to represent it.

- Bonus:
Replace the binary values of the leaves with numerical values, combine this with a tileset. And there you have it, you have generated your tilemap through a quadtree.

**Definition of a QuadTree:**

A QuadTree, or quaternary tree (Q-tree), is a tree data structure in which each node has four children. QuadTrees are most commonly used to partition a two-dimensional space by recursively subdividing it into four nodes.

![img.png](files/quadtree.png)

There are several types of QuadTrees. In our case, it is a "region" QuadTree.

The "region" QuadTree represents a partition of the two-dimensional space by breaking down the region into four equal quadrants, then each quadrant into four sub-quadrants, and so on, with each "leaf node" containing data corresponding to a specific sub-region. Each tree node has exactly either four children or none (in the case of a leaf node).

Each node has four elements, and this is a well-known technique for image encoding. To simplify, the images are square, in black and white, and have sides of 2^n.

**Project Installation:**

- 1 - Clone the repository:

```git clone https://github.com/Ptitlu42/python-exercices-ludiques-arbre-quaternaire.git```

- 2 - Navigate to the folder:

```cd python-exercices-ludiques-arbre-quaternaire```

- 3 - Activate the virtual environment:

```source env/bin/activate```

- 4 - Run the tests:

```pytest tests/test_quadtree.py```

  **Graphical Visualization:**

- To choose the *txt* file to use, change the *filename* variable (line 6 of /src/quadtree.py)

- Run the Python file:

```python3 src/quadtree.py```
