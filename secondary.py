class Heap(object):

    def insert(self, value: int) -> None:
        pass

    def find_min(self) -> int:
        pass

    def delete_min(self) -> int:
        pass

    def decrease_key(self, current_value: int, new_value :int) -> None:
        pass

    def has_nested_arrays(self) -> bool:
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        pass

def remove_empty_items(lst):
    if not isinstance(lst, list):
        return lst
    else:
        return [x for x in map(remove_empty_items, lst) if (x != [] and x != '')]

def add(lst: list, second_lst: list):
    for item in lst:
        if item > second_lst[0]:
            item.append(second_lst)
    return [x for x in map(add, lst) if (x != [] and x != '')]

def ln(x):
    n = 1000.0
    return n * ((x ** (1/n)) - 1)

class FibonacciHeap(Heap):

    def __init__(self):
        self.nodes = []

    def insert(self, value: int) -> None:
        self.nodes.append([value])

    def find_min(self) -> int:
        return min(self.nodes)[0]

    def delete_min(self) -> int:
        searched = self.find_min()
        for node in self.nodes:
            try:
                node.remove(searched)
            except ValueError:
                pass

        self.nodes = remove_empty_items(self.nodes)
        return searched

    def has_nested_arrays(self) -> bool:
        for node in self.nodes:
            if len(node) > 1:
                return True
        return False

    def merge(self, second_heap: Heap) -> None:
        if self.has_nested_arrays() == False and second_heap.has_nested_arrays() == False:
            self.nodes = self.nodes + second_heap.nodes
            return
        else:
            self.nodes = add(self.nodes, second_heap.nodes)

fibonacci_heap = FibonacciHeap()
fibonacci_heap.insert(10)
fibonacci_heap.insert(6)
fibonacci_heap.insert(4)
fibonacci_heap.insert(8)

secondary_heap = FibonacciHeap()
secondary_heap.insert(4)
secondary_heap.insert(2)

if fibonacci_heap.find_min() == 4:
    print("Find_min fonctionnel.")

if fibonacci_heap.delete_min() == 4:
    if fibonacci_heap.find_min() == 6:
        print("Delete_min fonctionnel.")

fibonacci_heap.merge(secondary_heap)

if fibonacci_heap.find_min() == 2:
    print("Merge fonctionnel.")