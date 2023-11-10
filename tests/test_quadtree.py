import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from src import QuadTree, QuadTreeDisplay

def test_sample():
    filename = "files/quadtree.txt"
    q = QuadTree.fromFile(filename)
    assert q.depth == 4

def test_single():
    filename = "files/quadtree_easy.txt"
    q = QuadTree.fromFile(filename)
    assert q.depth == 1

def test_perso():
    filename = "files/quadtree_perso.txt"
    q = QuadTree.fromFile(filename)
    assert q.depth == 6

def test_big():
    filename = "files/quadtree_big.txt"
    q = QuadTree.fromFile(filename)
    assert q.depth == 25

