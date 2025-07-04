class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def _get_hash(self, key):
        return sum(ord(char) for char in key) % self.size

    def add(self, key, value):
        h = self._get_hash(key)
        # Update if key exists
        for idx, (k, v) in enumerate(self.table[h]):
            if k == key:
                self.table[h][idx] = (key, value)
                return
        self.table[h].append((key, value))  # Handle collision by appending

    def get(self, key):
        h = self._get_hash(key)
        for k, v in self.table[h]:
            if k == key:
                return v
        return None

    def delete(self, key):
        h = self._get_hash(key)
        for idx, (k, _) in enumerate(self.table[h]):
            if k == key:
                del self.table[h][idx]
                return True
        return False

    def print_table(self):
        for idx, items in enumerate(self.table):
            print(f"{idx}: {items}")
ht = HashTable()
ht.add("apple", 10)
ht.add("grape", 20)  # May collide with "apple"
ht.print_table()
