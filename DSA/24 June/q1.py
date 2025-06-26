    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def insert_at_beginning(self, data):
            node = Node(data)
            node.next = self.head
            self.head = node

        def insert_at_end(self, data):
            node = Node(data)
            if not self.head:
                self.head = node
                return
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

        def insert_at_index(self, index, data):
            if index == 0:
                self.insert_at_beginning(data)
                return
            temp = self.head
            for _ in range(index - 1):
                if not temp:
                    raise IndexError("Index out of range")
                temp = temp.next
            node = Node(data)
            node.next = temp.next
            temp.next = node

        def delete_at_beginning(self):
            if not self.head:
                raise IndexError("List is empty")
            self.head = self.head.next

        def delete_at_end(self):
            if not self.head:
                raise IndexError("List is empty")
            if not self.head.next:
                self.head = None
                return
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None

        def delete_at_index(self, index):
            if index == 0:
                self.delete_at_beginning()
                return
            temp = self.head
            for _ in range(index - 1):
                if not temp or not temp.next:
                    raise IndexError("Index out of range")
                temp = temp.next
            temp.next = temp.next.next

        def delete_value(self, value):
            if not self.head:
                return
            if self.head.data == value:
                self.head = self.head.next
                return
            temp = self.head
            while temp.next:
                if temp.next.data == value:
                    temp.next = temp.next.next
                    return
                temp = temp.next

        def to_list(self):
            result = []
            temp = self.head
            while temp:
                result.append(temp.data)
                temp = temp.next
            return result


    # ---------- TEST CASES ----------

    def test():
        ll = LinkedList()
        
        # Insert at beginning
        ll.insert_at_beginning(3)
        ll.insert_at_beginning(2)
        assert ll.to_list() == [2, 3]
        
        # Insert at end
        ll.insert_at_end(4)
        ll.insert_at_end(5)
        assert ll.to_list() == [2, 3, 4, 5]
        
        # Insert at index
        ll.insert_at_index(2, 10)
        ll.insert_at_index(0, 1)
        assert ll.to_list() == [1, 2, 3, 10, 4, 5]
        
        # Delete at beginning
        ll.delete_at_beginning()
        ll.delete_at_beginning()
        assert ll.to_list() == [3, 10, 4, 5]
        
        # Delete at end
        ll.delete_at_end()
        ll.delete_at_end()
        assert ll.to_list() == [3, 10]
        
        # Delete at index
        ll.insert_at_end(20)
        ll.insert_at_end(30)
        ll.delete_at_index(1)
        assert ll.to_list() == [3, 20, 30]
        
        # Delete value
        ll.delete_value(20)
        ll.delete_value(3)
        assert ll.to_list() == [30]
        
        print("All test cases passed.")

    test()




