class Array:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        self.data.insert(index, value)

    def delete(self, index):
        del self.data[index]

    def access(self, index):
        return self.data[index]


def test_array():
    arr = Array()
    
    # Insert elements
    arr.insert(0, 10)
    arr.insert(1, 20)
    arr.insert(1, 15)  # Insert 15 at index 1

    # Access elements
    print("Accessing elements:")
    print(arr.access(0))  # Output: 10
    print(arr.access(1))  # Output: 15
    print(arr.access(2))  # Output: 20

    # Delete element
    arr.delete(1)  # Remove 15
    print("After deletion:")
    print(arr.access(1))  # Output: 20

    print("All Array tests passed!")


# Test Array
test_array()
