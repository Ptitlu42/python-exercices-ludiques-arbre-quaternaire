## Objective

Welcome to the fascinating world of QuadTrees! 🌳 In this project, our goal is to bring to life a QuadTree based on the data from files/quadtree.txt and showcase it through a sleek graphical interface using the TkQuadTree class.

## Main tasks

1 - Generate QuadTree:

- Kick off the journey by generating a QuadTree from the mystical quadtree.txt.

2 - Graphical Interface:

- Unleash the power of visualization with the TkQuadTree class, creating a captivating graphical representation of our QuadTree.🖼️

**Bonus Challenge:**

If you're feeling adventurous, embark on the bonus quest!

- Transform binary leaf values into numerical treasures.
- Conjure a tileset to breathe life into your QuadTree, crafting a mesmerizing tilemap.

## Definition of a QuadTree

Behold the QuadTree, a magical data structure! 🌲 It divides a two-dimensional space into four nodes, recursively breaking down regions into quadrants. Our QuadTree, a "region" QuadTree, creates a symphony of sub-regions, with each leaf node holding secrets of a specific realm.

![img.png](files/quadtree.png)

There are several types of QuadTrees. In our case, it is a "region" QuadTree.

The "region" QuadTree represents a partition of the two-dimensional space by breaking down the region into four equal quadrants, then each quadrant into four sub-quadrants, and so on, with each "leaf node" containing data corresponding to a specific sub-region. Each tree node has exactly either four children or none (in the case of a leaf node).

Each node has four elements, and this is a well-known technique for image encoding. To simplify, the images are square, in black and white, and have sides of 2^n.

## Project Installation

Unveil the magic on your local realm with these incantations:

- 1 - Clone the repository:

```git clone https://github.com/Ptitlu42/python-exercices-ludiques-arbre-quaternaire.git```

- 2 - Navigate to the folder:

```cd python-exercices-ludiques-arbre-quaternaire```

- 3 - Activate the virtual environment:

```source env/bin/activate```

- 4 - Run the tests:

```pytest tests/test_quadtree.py```

  **Graphical Visualization:**

Dive into the enchanting world of visualization:

Choose Your Destiny:

- Select the *txt* file of your choosing by modifying the filename variable (located at  line 6 of  📂 */src/quadtree.py*).
  
- Run the Magic Spell:

```python3 src/quadtree.py```

Witness the QuadTree unfold its branches and reveal the secrets within!✨
