# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # set a variable hash to the prime number 5381
        # loop through every character in the string
            # set hash to the sum of  5 bitwise shift left operation on hash plus hash 
            # plus the character code of the present character
        # return hash and bitwise and the hexadecimal constant 0xFFFFFFFF
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # call self._hash_mod(key) and get the index of the insertion
        index = self._hash_mod(key)

        # check to see if the value at the index is not None
        if self.storage[index] is not None:
            # create a new LinkedPair class with the key and value
            new_pair = LinkedPair(key, value)

            # store the head of the linked list in a variable
            current_pair = self.storage[index]

            # if current_pair key == key simply replace the value with value and return
            if current_pair.key == key:
                current_pair.value = value
                return

            # loop through to the end of the linked list and insert the new linked pair
            while current_pair.next is not None:
                # move to the next pair
                current_pair = current_pair.next

                # if current_pair key == key simply replace the value with value and return
                if current_pair.key == key:
                    current_pair.value = value
                    return

            # set the next pair to the new_pair
            current_pair.next = new_pair
        # otherwise, make a LinkedPair with the key, value and set it at that index
        else:
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # call self._hash_mod(key) and get the index of the insertion
        index = self._hash_mod(key)

        # check to see if the value at the index is not None
        if self.storage[index] is not None:
            # set the current pair to the head of the linked list
            current_pair = self.storage[index]

            # if current pair key == key or there is no next pair, set the current index to current_pair next
            if current_pair.key == key or current_pair.next is None:
                self.storage[index] = current_pair.next
            # otherwise
            else:
                # loop through the linked list
                while current_pair is not None:
                    # let next pair = current pair next
                    next_pair = current_pair.next

                    # if next pair key == key
                    if next_pair.key == key:
                        # set current pair next to next pair next
                        current_pair.next = next_pair.next

                    # set current pair to current pair next
                    current_pair = current_pair.next
        # otherwise, print a warning
        else:
            print("No match for that key!")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # call self._hash_mod(key) and get the index of the insertion
        index = self._hash_mod(key)

        # check to see if the value at the index is not None
        if self.storage[index] is not None:
            # let current pair hold the head of the linked list
            current_pair = self.storage[index]

            # loop through the linked list to find the key
            while current_pair is not None:
                # if the current linked pair key == key return the value
                if current_pair.key == key:
                    return current_pair.value

                # increment current_pair
                current_pair = current_pair.next

            # return None is a key matching the input key is not found
            return None

        # otherwise return None
        else:
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # double the size of self.capacity
        self.capacity *= 2
        # let old_storage hold self.storage
        old_storage = self.storage
        # point self.storage to a list of capacity self.capacity
        self.storage = [None] * self.capacity

        # loop through old_storage and rehash every key/value pair
        for item in old_storage:
            # if item is not None
            if item is not None:
                # set the head of the linked list to current_pair
                current_pair = item

                # loop through the linked list
                while current_pair is not None:
                    # call self.insert with the key/value of the linked pair
                    self.insert(current_pair.key, current_pair.value)
                    # set current_pair to current_pair next
                    current_pair = current_pair.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    ht.insert("line_4", "Linked list does not save the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print(ht.retrieve("line_4"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print(ht.retrieve("line_4"))

    print("")
