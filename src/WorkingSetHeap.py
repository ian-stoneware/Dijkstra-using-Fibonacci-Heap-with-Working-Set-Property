import math  # Add this line at the top of the file


class WorkingSetHeap:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val  # Node index
            self.degree = 0
            self.parent = None
            self.child = None
            self.mark = False
            self.next = self
            self.prev = self

    def __init__(self):
        self.min = None
        self.num_nodes = 0
        self.heaps = []  # List of sub-heaps

    def insert(self, key, val):
        """Insert a new node with the given key and value."""
        new_node = self.Node(key, val)
        if self.min is None:
            self.min = new_node
        else:
            self._link(self.min, new_node)
            if key < self.min.key:
                self.min = new_node
        self.num_nodes += 1
        return new_node

    def _link(self, a, b):
        """Link two nodes together in the doubly circular linked list."""
        a.prev.next = b
        b.prev = a.prev
        b.next = a
        a.prev = b

    def find_min(self):
        """Return the node with the minimum key."""
        return self.min

    def delete_min(self):
        """Remove and return the node with the minimum key."""
        z = self.min
        if z is not None:
            if z.child:
                children = []
                child = z.child
                while True:
                    children.append(child)
                    child = child.next
                    if child == z.child:
                        break
                for child in children:
                    self._link(z, child)
                    child.parent = None

            self._link(z.prev, z.next)
            if z == z.next:
                self.min = None
            else:
                self.min = z.next
                self._consolidate()

            self.num_nodes -= 1
        return z

    def _consolidate(self):
        """Consolidate the heap after a delete-min operation."""
        max_degree = int(math.log(self.num_nodes) / math.log(2)) + 1  # Fix here, import math
        aux = [None] * (max_degree + 1)

        node = self.min
        while True:
            degree = node.degree
            while aux[degree]:
                other = aux[degree]
                if other.key < node.key:
                    node, other = other, node
                self._link(node, other)
                aux[degree] = None
                degree += 1
            aux[degree] = node
            node = node.next
            if node == self.min:
                break

        self.min = None
        for node in aux:
            if node:
                if self.min is None or node.key < self.min.key:
                    self.min = node

    def decrease_key(self, node, new_key):
        """Decrease the key of a node."""
        if new_key > node.key:
            raise ValueError("New key is greater than the current key")
        node.key = new_key
        parent = node.parent
        if parent and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)

        if node.key < self.min.key:
            self.min = node

    def _cut(self, node, parent):
        """Cut a node from its parent."""
        if node == parent.child:
            parent.child = node.next if node != parent.child else None
        parent.degree -= 1
        self._link(self.min, node)
        node.parent = None
        node.mark = False

    def _cascading_cut(self, node):
        """Perform cascading cuts."""
        parent = node.parent
        if parent:
            if not node.mark:
                node.mark = True
            else:
                self._cut(node, parent)
                self._cascading_cut(parent)
