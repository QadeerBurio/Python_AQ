class HashTable:
    def __init__(self):
        self.MAX = 100
        self.table = [None] * self.MAX

    def _get_hash(self, key):
        hash_val = 0
        for char in key:
            hash_val += ord(char)
        return hash_val % self.MAX

    def add(self, key, value):
        h = self._get_hash(key)
        if self.table[h] is None:
            self.table[h] = []
        # Update value if key exists
        for idx, (k, v) in enumerate(self.table[h]):
            if k == key:
                self.table[h][idx] = (key, value)
                return
        self.table[h].append((key, value))

    def get(self, key):
        h = self._get_hash(key)
        if self.table[h]:
            for k, v in self.table[h]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        h = self._get_hash(key)
        if self.table[h]:
            for idx, (k, _) in enumerate(self.table[h]):
                if k == key:
                    del self.table[h][idx]
                    return True
        return False
ht = HashTable()
ht.add("apple", 100)
ht.add("banana", 80)

print(ht.get("apple"))     # Output: 100
ht.delete("banana")
print(ht.get("banana"))    # Output: None