class Patient:
    """Represents a patient with a name and urgency (1-10, 1 most urgent)."""
    def __init__(self, name: str, urgency: int):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(urgency, int) or not (1 <= urgency <= 10):
            raise ValueError("urgency must be an integer between 1 and 10")
        self.name = name
        self.urgency = urgency

    def __repr__(self):
        return f"Patient(name={self.name!r}, urgency={self.urgency})"



class MinHeap:
    """Min-heap of Patient objects, ordered by urgency (lower is higher priority)."""
    def __init__(self):
        self.data = []

    def _parent(self, idx):
        return (idx - 1) // 2 if idx > 0 else None

    def _left(self, idx):
        return 2 * idx + 1

    def _right(self, idx):
        return 2 * idx + 2

    def heapify_up(self, index: int) -> None:
        while index > 0:
            parent_idx = self._parent(index)
            if parent_idx is None:
                break
            if self.data[index].urgency < self.data[parent_idx].urgency:
                self.data[index], self.data[parent_idx] = self.data[parent_idx], self.data[index]
                index = parent_idx
            else:
                break

    def heapify_down(self, index: int) -> None:
        n = len(self.data)
        while True:
            left = self._left(index)
            right = self._right(index)
            smallest = index
            if left < n and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < n and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right
            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break

    def insert(self, patient: Patient) -> None:
        if not isinstance(patient, Patient):
            raise TypeError("insert expects a Patient instance")
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self) -> None:
        print("Current Queue:")
        for p in self.data:
            print(f"- {p.name} ({p.urgency})")

    def peek(self):
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()
        root = self.data[0]
        # Move last to root and heapify down
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return root




if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()

    next_up = heap.peek()
    print("Next up:", next_up.name, next_up.urgency)

    served = heap.remove_min()
    print("Served:", served.name)
    heap.print_heap()

    # Edge cases
    empty_heap = MinHeap()
    print("Peek empty:", empty_heap.peek())
    print("Remove empty:", empty_heap.remove_min())

