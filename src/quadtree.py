from __future__ import annotations
import pygame

from pygame.locals import *

filename = "files/quadtree.txt"

class QuadTree:
    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
        self.hg = hg
        self.hd = hd
        self.bd = bd
        self.bg = bg

    @property
    def depth(self) -> int:
        if self.hg is None:
            return 0
        return 1 + max(self.hg.depth, self.hd.depth, self.bd.depth, self.bg.depth)

    @staticmethod
    def fromFile(filename: str) -> QuadTree:
        """
        Creates and returns a QuadTree instance from serialized data in the specified file.

        Args:
        - filename (str): The path to the file containing serialized data.

        Returns:
        - QuadTree: QuadTree instance created from the file data.

        Raises:
        - IOError: If the file cannot be opened or read.
        - ValueError: If the file data cannot be properly evaluated or if the structure is not compliant with a QuadTree.
        - Exception: Any other exception during file opening or data evaluation.
        """
        with open(filename, 'r') as file:
            data = eval(file.read())
        return QuadTree.fromList(data)

    @staticmethod
    def fromList(data: list) -> QuadTree:
        """
         Creates and returns a QuadTree instance from a list representing a hierarchical structure.

        Args:
        - data (list): A list representing a hierarchical structure of QuadTree nodes. Should have four elements.

        Returns:
        - QuadTree: QuadTree instance created from the list data.

        Raises:
        - ValueError: If the input data is not a list or does not have exactly four elements.
        
        """
        if isinstance(data, list):
            if len(data) == 4:
                hg, hd, bd, bg = data
                return QuadTree(
                    QuadTree.fromList(hg), QuadTree.fromList(hd),
                    QuadTree.fromList(bd), QuadTree.fromList(bg)
                )
        return QuadTree(None, None, None, None)
        
    @staticmethod
    def fromFileToDisplay(filename: str) -> QuadTree:
        """
        TODO : Temporary method to dislay a quadtree.
        """
        with open(filename, 'r') as file:
            data = eval(file.read())
        return QuadTree.fromListToDisplay(data)

    @staticmethod
    def fromListToDisplay(data: list) -> QuadTree:
        """
        TODO : Temporary method to dislay a quadtree.
        """
        if isinstance(data, list):
            if len(data) == 4:
                hg, hd, bd, bg = data
                return QuadTree(
                    QuadTree.fromListToDisplay(hg), QuadTree.fromListToDisplay(hd),
                    QuadTree.fromListToDisplay(bd), QuadTree.fromListToDisplay(bg)
                )
        else:
            return bool(data)

class QuadTreeDisplay:

    def paint(self, surface, quadtree, x, y, size):
        if isinstance(quadtree, QuadTree):
            half_size = size // 2
            self.paint(surface, quadtree.hg, x, y, half_size)
            self.paint(surface, quadtree.hd, x + half_size, y, half_size)
            self.paint(surface, quadtree.bd, x + half_size, y + half_size, half_size)
            self.paint(surface, quadtree.bg, x, y + half_size, half_size)
        else:
            color = (255, 255, 255) if quadtree else (0, 0, 0)
            pygame.draw.rect(surface, color, (x, y, size, size))

if __name__ == '__main__':
    window_size = 300
    pygame.init()
    screen = pygame.display.set_mode((window_size, window_size))
    pygame.display.set_caption("Quadtree")

    quadtree = QuadTree.fromFileToDisplay(filename)

    quadtree_display = QuadTreeDisplay()  

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        screen.fill((0, 0, 0))

        quadtree_display.paint(screen, quadtree, 0, 0, window_size)
        pygame.display.flip()

    pygame.quit()
