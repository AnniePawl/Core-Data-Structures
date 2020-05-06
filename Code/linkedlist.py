#!python

# Initialize Node Class
class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

# Initialize LinkedList Class
class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) because it finds the length linearly  """
    
        node_count = 0 # initialize node count at 0 
        node = self.head # start at beginning of ll
        # Loop until the node is None (one past tail)
        while node is not None:
            node_count += 1 # increase node count
            node = node.next # skip to next node
        return node_count # now node_count reflect num of nodes

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) if list is empty or item is first
        Worst case running time: O(n) if index is later in list or not found"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))

        index_count = 0 # initialize at - 
        node = self.head # start at beginning of ll 
        while (0 <= index_count < self.size):
            if index_count == index: # when we reach index we're looking for, return node's data
                return node.data
            index_count += 1 # otherwise move onto next index and check again 
            node = node.next # reset node to equal next node

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) if list is empty or item is first
        Worst case running time: O(n) if index is later in list or not found"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
    
        elif (index == 0): # if index 0, simply add item to beginningg of linked list
            self.prepend(item)
        elif (index == self.size): # if index is length of linked list, simply add item to end of linked list
            self.append(item)
        
        else: # if neither of the above, create a new node for item
            new_node = Node(item)
            previous_node = self.head  # reset start of ll
            i = 0
            while i != (index - 1) and previous_node is not None:
                previous_node = previous_node.next
                i += 1
            next_node = previous_node.next
            new_node.next = next_node # reset next_node
            previous_node.next = new_node # reset new_node
            self.size += 1 # increase size

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case running time: O(1) because item is always inserted at the end"""
        new_node = Node(item) # make new node to hold item 
        if self.is_empty(): # check is ll is empty
            self.head = new_node # make new node the head
        else:
            self.tail.next = new_node # otherwise inert new node at end of ll 
        self.tail = new_node # make last node our new node
        self.size += 1 # increase size by one to reflect 

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case running time: O(1) because item is always inserted at the beginning"""
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
        # Update head to new node regardless
        self.head = new_node
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        node = self.head  # start at the head node
        # Loop until the node is None (one node past end)
        while node is not None:  
            # Check if this node's data satisfies given quality 
            if quality(node.data): 
                # exit if satisfied the quality
                return node.data 
            node = node.next  
        return None  # return None if we never find node that satisfies quality  

    def replace(self, old_data, new_data):
        """Replace the given old_data in this linked list with given new_data
        using the same node, or raise ValueError if old_data is not found.
        Best case running time: O(1) if list is empty or item is first
        Worst case running time: O(n) if old_data is later in list or not found"""
        node = self.head # start at head node
        found = None
        # Loop until the node is None (one past end)
        while node is not None:  
            # Check if this node's data satisfies quality
            if node.data == old_data:
                found = node # found node
                break
            # Skip to the next node
            node = node.next 
        if found == None: # if we never find node that satisfies quality, raise error 
            raise ValueError("value not found!")
        found.data = new_data

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) if list is empty or item is first
        Worst case running time: O(n) if item is not found or is later in the list"""
        node = self.head # start at head
        # Keep track of the node before node containing item
        previous = None
        
        found = False # Create variable to track if we have found item
        # Loop until we have found item or the node is None
        while not found and node is not None:
            if node.data == item: #Check if the node's data matches item
                found = True # update found if we find matching item
            else:
                previous = node   # Skip to the next node
                node = node.next 
        # Check if we found the given item or we never did and reached the tail
        if found:
            self.size -= 1
            # Check if we found node in the middle of ll
            if node is not self.head and node is not self.tail:
                # Update the previous node to skip around the found node
                previous.next = node.next
                node.next = None

            if node is self.head: # check if node found at head
                self.head = node.next # update head
                node.next = None

            if node is self.tail: # check if node at tail
                # Check if node exists before found node
                if previous is not None:
                    previous.next = None
                self.tail = previous # update tail 
        else:
            # otherwise raise error
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()