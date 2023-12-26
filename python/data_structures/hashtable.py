class Hashtable:
    """
    Create object that will function like a dictionary.
    """

    def __init__(self, size: int=200):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash(self, key):
        """
        Input immutable key.
        Output hash of key.
        """
        try:
            key_hash = hash(key) % self.size
            return key_hash
        except Exception as err:
            raise ValueError(f"Hash function failed. {err}")


    def set(self, key, value) -> None:
        """
        Input immutable key and value pair.
        Adds to Hashtable instance.
        No output.
        """
        key_hash = self.hash(key)
        for pairs in self.buckets[key_hash]:
            if pairs[0] == key:
                raise ValueError('Dictionary can only contain unique keys.')
        self.buckets[key_hash].append((key, value))

    def has(self, key) -> bool:
        """
        Input immutable key.
        Output boolean if key exists inside Hashtable instance.
        """
        key_hash = self.hash(key)
        for pairs in self.buckets[key_hash]:
            if pairs[0] == key:
                return True
        return False

    def get(self, key):
        """
        Input immutable key.
        Output is value that matches key in Hashtable instance or None if no match exists.
        """
        key_hash = self.hash(key)
        for pairs in self.buckets[key_hash]:
            if pairs[0] == key:
                return pairs[1]
        return None

    def keys(self):
        """
        Output returns list of keys in Hashtable instance.
        """
        list_keys = []
        for pairs in self.buckets:
            for pair in pairs:
                list_keys.append(pair[0])
        return list_keys

    def __str__(self) -> str:
        """
        Output string representation of Hashtable instance.
        """
        list_return = []
        for pairs in self.buckets:
            if pairs:
                list_return.append(pairs)
        return str(list_return)



if __name__ == "__main__":
    hashtable = Hashtable(1024)
    # hashtable.set("apple", "Used for apple sauce")
    # hashtable.set("ahmad", 30)
    # hashtable.set("silent", True)
    # hashtable.set("listen", "to me")
    # actual = []
    # for item in hashtable.buckets:
    #     if item:
    #         actual.append(item)
    # expected = [("apple", "Used for apple sauce"), ("silent", True), ("listen", "to me"), ("ahmad", 30)]
    # print(actual)
    print(hashtable.hash(1))
    print(hashtable.hash(1025))
    hashtable.set(1,'test1')
    hashtable.set(1025,'test1025')
    print(hashtable)
