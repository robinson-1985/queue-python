class Node:
    
    def __init__(self, value, next, previous):
        self.value = value
        self.next = next
        self.previous = previous

        self.set_next(previous)

    def set_next(self, previous):
        if previous is not None:
            previous.next = self

    def print_desc(self):
        while self.previous != None:
            print(self.value)
            self = self.previous

        if self.previous == None:
            print(self.value)

    def print_asc(self):
        while self.next != None:
            print(self.value)
            self = self.next
        
        if self.next == None:
            print(self.value)


def queue():
    first = Node(value=1, next=None, previous=None)
    second = Node(value=2, next=None, previous=first)
    third = Node(value=3, next=None, previous=second)
    four = Node(value=4, next=None, previous=third)
    five = Node(value=5, next=None, previous=four)
    six = Node(value=6, next=None, previous=five)
    seven = Node(value=7, next=None, previous=six)
    eight = Node(value=8, next=None, previous=seven)
    nine = Node(value=9, next=None, previous=eight)
    ten = Node(value=10, next=None, previous=nine)

    return first, ten




if __name__ == "__main__":
    first, last = queue()

    print("Exibe do ultimo para o primeiro")
    #print_desc(last)
    last.print_desc()

    print("Exibe do primeiro para o ultimo")
    #print_asc(first)
    first.print_asc()