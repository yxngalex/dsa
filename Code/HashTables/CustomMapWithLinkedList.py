from Code.LinkedLists.CustomLinkedList import LinkedList


class CustomMap():
    def __init__(self, size):
        self.data = [None] * size

    # calculates an address with key's chracters unicode value and based on the len of an array it returns a hash_value
    def _hash(self, key):
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % len(
                self.data)  # ord, gets a unicode value for each character in key

        return hash_value

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = LinkedList([key, value])
        else:
            self.data[address].append([key, value])
        return self.data

    def get(self, key):
        address = self._hash(key)
        currentBucket = self.data[address]
        if currentBucket:
            current = currentBucket.head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next

    def keys(self):
        keysArr = []
        for i in range(len(self.data)):
            if self.data[i]:
                current = self.data[i].head
                while current:
                    keysArr.append(current.value[0])
                    current = current.next
        return keysArr

    def keysWithoutCollision(self):
        if not self.data:
            return None

        result = []

        for i in range(len(self.data)):
            if self.data[i] is not None:
                current = self.data[i].head
                while current:
                    result.append(current.value[0])
                    current = current.next
        return result


if __name__ == "__main__":
    map = CustomMap(50)
    map.set("grapes", 10000)
    map.set("apples", 54)
    map.set("oranges", 2)
    print(map.get('grapes'))
    print(map.keys())
    print(map.keysWithoutCollision())
