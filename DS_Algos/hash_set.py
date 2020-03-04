class HashSet:
    def __init__(self):
        self.size = 1_000
        self.buckets = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        return key % self.size
    
    def _index(self, key):
        bucket = self.buckets[self._hash(key)]

        for i, k in enumerate(bucket):
            if k == key:
                return bucket, i
        
        return bucket, -1
    
    def add(self, key):
        bucket, idx = self._index(key)

        if idx >= 0:
            return
        
        bucket.append(key)

    def contains(self, key):
        bucket, idx = self._index(key)

        return idx >= 0
    
    def remove(self, key):
        bucket, idx = self._index(key)

        if idx < 0:
            return
        
        bucket.remove(key)
