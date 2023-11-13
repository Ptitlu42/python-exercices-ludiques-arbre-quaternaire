from __future__ import annotations
import pygame

from pygame.locals import QUIT

filename = "files/quadtree.txt"

class QuadTree:
    """
    Definition of quadtree object
    """

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool \
        | QuadTree, bg: bool | QuadTree):
        self.hg = hg
        self.hd = hd
        self.bd = bd
        self.bg = bg

    @property
    def depth(self) -> int:
        """
        Returns the depth of the current node in a hierarchical structure.

        If the current node has no children (hg is None), the depth is 0.
        Otherwise, the depth is calculated as 1 plus the maximum depth among the
        left upper (hg), right upper (hd), right bottom (bd), and left bottom (bg) children.

        Returns:
            int: The depth of the current node in the hierarchy.
        """
        if self.hg is None:
            return 0
        return 1 + max(self.hg.depth, self.hd.depth, self.bd.depth, self.bg.depth)

    @staticmethod
    def from_file(filename: str) -> QuadTree:
        """
        Creates and returns a QuadTree instance from serialized data in the specified file.

        Args:
        - filename (str): The path to the file containing serialized data.

        Returns:
        - QuadTree: QuadTree instance created from the file data.

        Raises:
        - IOError: If the file cannot be opened or read.
        - ValueError: If the file data cannot be properly evaluated
        or if the structure is not compliant with a QuadTree.
        - Exception: Any other exception during file opening or data evaluation.
        """
        with open(filename, 'r', encoding="utf-8") as file:
            data = eval(file.read())
        return QuadTree.from_list(data)

    @staticmethod
    def from_list(data: list) -> QuadTree:
        """
         Creates and returns a QuadTree instance from a list representing a hierarchical structure.

        Args:
        - data (list): A list representing a hierarchical structure of
        QuadTree nodes. Should have four elements.

        Returns:
        - QuadTree: QuadTree instance created from the list data.

        Raises:
        - ValueError: If the input data is not a list or does not have exactly four elements.
        
        """
        if isinstance(data, list):
            if len(data) == 4:
                hg, hd, bd, bg = data
                return QuadTree(
                    QuadTree.from_list(hg), QuadTree.from_list(hd),
                    QuadTree.from_list(bd), QuadTree.from_list(bg)
                )
        return QuadTree(None,  None,  None,  None)

    @staticmethod
    def from_file_to_display(filename: str) -> QuadTree:
        """
        TODO : Temporary method to dislay a quadtree.
        """
        with open(filename, 'r') as file:
            data = eval(file.read())
        return QuadTree.from_list_to_display(data)

    @staticmethod
    def from_list_to_display(data: list) -> QuadTree:
        """
        TODO : Temporary method to dislay a quadtree.
        """
        if isinstance(data, list):
            if len(data) == 4:
                hg, hd, bd, bg = data
                return QuadTree(
                    QuadTree.from_list_to_display(hg), QuadTree.from_list_to_display(hd),
                    QuadTree.from_list_to_display(bd), QuadTree.from_list_to_display(bg)
                )
        else:
            return bool(data)

class QuadTreeDisplay:
    """
    Graphical representation of quadtree
    """
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
    WINDOWS_SIZE = 300
    pygame.init()
    screen = pygame.display.set_mode((WINDOWS_SIZE, WINDOWS_SIZE))
    pygame.display.set_caption("Quadtree")

    quadtree = QuadTree.from_file_to_display(filename)

    quadtree_display = QuadTreeDisplay()

    RUNNING = True
    while RUNNING:
        for event in pygame.event.get():
            if event.type == QUIT:
                RUNNING = False

        screen.fill((0, 0, 0))

        quadtree_display.paint(screen, quadtree, 0, 0, WINDOWS_SIZE)
        pygame.display.flip()

    pygame.quit()
