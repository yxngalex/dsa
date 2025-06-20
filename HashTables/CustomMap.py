class CustomMap():
    def __init__(self, size):
        self.data = [None] * size

    # calculates an address with key's chracters unicode value and based on the len of an array it returns a hash_value
    def _hash(self, key): 
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % len(self.data) # ord, gets a unicode value for each character in key

        return hash_value


    def set(self, key, value): #O(1)
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data

    def get(self, key): # Most of time, without collisions it's O(1), in this case it's O(n), since we're going through the loop 
        address = self._hash(key)
        currentBucket = self.data[address]
        if currentBucket:
            for i in range(len(currentBucket)):
                if currentBucket[i][0] == key:
                    return currentBucket[i][1]

    def keys(self):
        keysArr = []
        for i in range(len(self.data)):
            if self.data[i]:
                keysArr.append(self.data[i][0][0])
        return keysArr

    def keysWithoutCollision(self):
        if not self.data:
            return None

        result = []

        # loop through all the elements
        for i in range(len(self.data)):
            # if it's not an empty memory cell
            if self.data[i] and len(self.data[i]):
                # but also loop through all the potential collisions
                if len(self.data) > 1:
                    for j in range(len(self.data[i])):
                        result.append(self.data[i][j][0])
                else:
                    result.append(self.data[i][0])
        return result




if __name__ == "__main__":
    map = CustomMap(50)
    map.set("grapes", 10000)
    map.set("apples", 54)
    map.set("oranges", 2)
    print(map.get('grapes'))
    print(map.keys())
    print(map.keysWithoutCollision())
