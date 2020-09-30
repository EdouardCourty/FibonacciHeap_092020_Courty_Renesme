class Heap(object):
    def insert(self, value: int) -> None:
        pass

    def find_min(self) -> int:
        pass

    def delete_min(self) -> int:
        pass

    def decrease_key(self, current_value: int, new_value :int) -> None:
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        pass


class FibonacciHeap(Heap):

    nodes: list = []

    def insert(self, value: int) -> None:
        self.nodes.append(value)

    def find_min(self) -> int:
        return min(self.nodes)

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: Heap) -> None:
        """
        Fusionne deux arbres
        """
        pass

fibonacci_heap = FibonacciHeap()
fibonacci_heap.insert(10)
fibonacci_heap.insert(6)
fibonacci_heap.insert(4)
fibonacci_heap.insert(8)

secondary_heap = FibonacciHeap()
secondary_heap.insert(10)
secondary_heap.insert(6)
secondary_heap.insert(4)
secondary_heap.insert(2)

if fibonacci_heap.find_min() == 4:
    print("Find_min fonctionnel.")
else:
    print("Find_min non fonctionnel")

fibonacci_heap.delete_min()

if fibonacci_heap.find_min() == 8:
    print("Delete_min fonctionnel.")
else:
    print("Delete_min non fonctionnel")

fibonacci_heap.merge(secondary_heap)

if fibonacci_heap.find_min() == 2:
    print("Merge fonctionnel.")
else:
    print("Merge non fonctionnel")