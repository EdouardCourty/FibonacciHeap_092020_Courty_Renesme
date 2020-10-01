class Heap(object):
    class Node:
        def add_node(self, node):
            pass

    def insert(self, value: int) -> None:
        pass

    def find_min(self) -> int:
        pass

    def delete_min(self) -> int:
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        pass

def find_min_node_in_node_list(node_list: list):
    if not isinstance(node_list, list):
        raise ValueError("You must input a Node List.")
    minimal = None
    for node in node_list:
        if node_list.index(node) != 0:
            value_upper = node.value
            value_lower = node_list[node_list.index(node)-1].value
            if value_upper < value_lower:
                minimal = value_upper
            else:
                minimal = value_lower
    return [node for node in node_list if node.value == minimal][0]

def return_smallest_node_after_lowest(node_list: list):
    if not isinstance(node_list, list):
        raise ValueError("You must input a Node List.")
    lowest_node = find_min_node_in_node_list(node_list)
    clone_list = [node for node in node_list if node.value != lowest_node.value]
    minimal = None
    for node in clone_list:
        if clone_list.index(node) > 0:
            value_upper = node.value
            value_lower = clone_list[clone_list.index(node)-1].value
            if value_upper < value_lower:
                minimal = value_upper
            else:
                minimal = value_lower
    return [node for node in clone_list if node.value == minimal][0]

def is_even(nbr: int):
    if nbr % 2 == 0:
        return True
    else:
        return False

def get_number_of_same_count_nodes(node_list: list):
    if not isinstance(node_list, list):
        raise ValueError("You must input a Node List.")
    return 2
    highest_count = 1
    for node in node_list:
        if node.count > highest_count:
            highest_count = node.count



class FibonacciHeap(Heap):
    class Node(Heap.Node):
        def __init__(self, value: int):
            if not isinstance(value, int):
                raise ValueError("You must input an Integer value.")
            self.children = []
            self.value  = value
            self.count = 1

        def add_node(self, node):
            if not isinstance(node, Heap.Node):
                raise ValueError("You must input a Node.")
            self.children.append(node)
            self.count += 1

    def __init__(self):
        self.nodes: list = []
        self.min_node = None

    def insert(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("You must input an Integer value.")
        new_node = self.Node(value)
        self.nodes.append(new_node)
        if self.min_node is None or self.min_node.value > new_node.value:
            self.min_node = new_node

    def find_min_node(self) -> Node:
        return self.min_node

    def find_min(self) -> int:
        return self.find_min_node().value

    def delete_min_node(self) -> Node:
        for node in self.nodes:
            if node.value == self.min_node.value: # Found the minimum Node
                self.nodes += node.children
                self.nodes.remove(node)
                self.min_node = find_min_node_in_node_list(self.nodes)
                return node

    def delete_min(self) -> int:
        min_value = self.min_node.value
        self.delete_min_node()
        return min_value

    def merge(self, second_heap: Heap) -> None:
        if not isinstance(second_heap, Heap):
            raise ValueError("You must input a Heap to be merged.")
        if self.min_node.value > second_heap.min_node.value:
            self.min_node.value = second_heap.min_node.value
        self.nodes += second_heap.nodes

    def consolidate(self):
        while is_even(get_number_of_same_count_nodes(self.nodes)):
            second_smallest_node = return_smallest_node_after_lowest(self.nodes)
            self.nodes.remove(second_smallest_node)
            new_node = self.delete_min_node()
            if new_node is None:
                break
            new_node.add_node(second_smallest_node)
            self.nodes.append(new_node)

fibonacci_heap = FibonacciHeap()
fibonacci_heap.insert(10)
fibonacci_heap.insert(6)
fibonacci_heap.insert(4)
fibonacci_heap.insert(8)

secondary_heap = FibonacciHeap()
secondary_heap.insert(5)
secondary_heap.insert(3)
secondary_heap.insert(8)
secondary_heap.insert(1)
secondary_heap.insert(2)

if fibonacci_heap.find_min() == 4:
    print("Find_min fonctionnel.")

if fibonacci_heap.delete_min() == 4:
    if fibonacci_heap.find_min() == 6:
        print("Delete_min fonctionnel.")

fibonacci_heap.merge(secondary_heap)

fibonacci_heap.consolidate()

if fibonacci_heap.find_min() == 2:
    print("Merge fonctionnel.")
