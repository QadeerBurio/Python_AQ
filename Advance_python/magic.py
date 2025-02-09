# Q:1--> __init

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("AQ_Khan", 20)
print(p.name, p.age)

# Q:2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"


p = Person("AQ_Khan", 20)
print(str(p))
print(repr(p))

# Q:3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(2, 3)
p2 = Point(4, 5)
result = p1 + p2
print(result)  # Output: Point(6, 8)

# Q:4 __len__

class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


my_list = MyList([1, 2, 3,5,8,9])
print(len(my_list))


# Q:5
class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]


my_list = MyList([1, 2, 3])
print(my_list[1])  # Output: 2


# Q:6

class Adder:
    def __init__(self, value):
        self.value = value

    def __call__(self, x):
        return self.value + x


adder = Adder(10)
print(adder(5))  # Output: 15


# Q:7

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


for num in Counter(1, 3):
    print(num)
# Output: 1, 2, 3


# Q:8  __eq__, __lt__, __gt__

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age


p1 = Person("Alice", 30)
p2 = Person("Bob", 30)
print(p1 == p2)  # Output: True (since their ages are the same)


# Q: 9  __enter__ and __exit__:

class OpenFile:
    def __init__(self, filename, mode):
        self.file = open(filename, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


with OpenFile('test.txt', 'w') as f:
    f.write('Hello, World!')


# Q:10

class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} has been deleted.")


p = Person("Alice")
del p
# Output: Alice has been deleted.





























# Method	Operation or Action
# __init__	Object initialization (constructor)
# __str__	String conversion (for str() and print())
# __repr__	Developer-friendly representation (for repr())
# __add__	Addition (+)
# __len__	Length (len())
# __getitem__	Indexing (obj[key])
# __setitem__	Item assignment (obj[key] = value)
# __delitem__	Item deletion (del obj[key])
# __call__	Callable objects (calling objects like functions)
# __eq__	Equality comparison (==)
# __iter__	Iteration (used with for loops)
# __enter__	Context management (with statement)
# __exit__	Exit from with block
