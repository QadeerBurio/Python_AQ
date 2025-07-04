class remoteControl:
    def __init__(self):
        self.channels=["HBD","cnn","KTN","GEO NEWS"]
        self.index=-1

    def __iter__(self):
        return self

    def __next__(self):
        self.index+=1
        if self.index==len(self.channels):
            raise StopIteration

        return self.channels[self.index]

r=remoteControl()
itr=iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))



# Code 2


class CustomIterator:
    def __init__(self, data):
        """Initialize the iterator with a data collection."""
        if not isinstance(data, (list, tuple, dict)):
            raise TypeError("Only list, tuple, and dictionary types are supported.")
        self.data = data
        self.index = 0
        self.keys = list(data.keys()) if isinstance(data, dict) else None

    def __iter__(self):
        """Returns the iterator object itself."""
        return self

    def __next__(self):
        """Returns the next item in the collection."""
        if self.keys:  # If dictionary, iterate over keys
            if self.index < len(self.keys):
                key = self.keys[self.index]
                self.index += 1
                return key, self.data[key]
            else:
                raise StopIteration
        else:  # If list or tuple, iterate over elements
            if self.index < len(self.data):
                item = self.data[self.index]
                self.index += 1
                return item
            else:
                raise StopIteration

# Sample collections
my_list = ['200$', '200$', '200', '300', '300']
my_tuple = ('HUB', 'DANI', 'HASSNAIN', 'ADNAN','AQ_KHAN')
my_dict = {'name': 'AQ', 'age': 22, 'city': 'Hyderabad'}

# Iterating over a list
print("Iterating over a list:")
list_iterator = CustomIterator(my_list)
for item in list_iterator:
    print(item)

# Iterating over a tuple
print("\nIterating over a tuple:")
tuple_iterator = CustomIterator(my_tuple)
for item in tuple_iterator:
    print(item)

# Iterating over a dictionary
print("\nIterating over a dictionary:")
dict_iterator = CustomIterator(my_dict)
for key, value in dict_iterator:
    print(f"{key}: {value}")



