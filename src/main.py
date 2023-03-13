class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data, self.top)
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        popped = self.top.data
        self.top = self.top.next_node
        return popped

    def peek(self):
        if self.top is None:
            return None
        return self.top.data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data):
        '''добавляет новый узел в начало связанного списка'''
        new_node = Node(data, self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def insert_at_end(self, data):
        '''добавляет новый узел в конец связанного списка'''
        new_node = Node(data, None)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def print_ll(self):
        '''выводит все данные из списка в консоль'''
        ll_string = ''
        node = self.head
        if node is None:
            return 'None'
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string
