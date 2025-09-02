class CustomArray:
    def __init__(self):
        self.len = 0
        self.data = {}

    def get(self, index): #O(1)
        return self.data.get(index, None) # Returns None

    def push(self, item): #O(1)
        self.data[self.len] = item
        self.len += 1
        return self.len

    def pop(self): #O(1)
        if self.len == 0:
            return None

        last_index = self.len - 1
        item = self.data[last_index]
        del self.data[last_index]
        self.len -= 1
        return item

    def delete(self, index): #O(n)
        if index >= self.len or index < 0:
            return None

        item = self.data[index]

        for i in range(index, self.len - 1):
            self.data[i] = self.data[i+1]

        del self.data[self.len-1] # delete last element (duplicate)
        self.len -= 1

        return item


    def __str__(self):
        return f"CustomArray(length={self.len}, elements={self.data})"

def main():
    my_arr = CustomArray()
    my_arr.push('hi')
    my_arr.push('you')
    my_arr.push('!')
    my_arr.push('are')
    my_arr.push('nice')
    print(my_arr)
    print(my_arr.delete(2))
    print(my_arr)

if __name__ == "__main__":
    main()

