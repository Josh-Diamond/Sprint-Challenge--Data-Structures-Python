from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity > self.storage.__len__(): # if RingBuffer has room, Add newest item to head
            self.storage.add_to_head(item)
        else:
            self.storage.remove_from_tail()
            self.storage.add_to_head(item)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        num = 0
        while num < self.storage.__len__(): # loop through storage
            current_head = self.storage.head # grab head
            list_buffer_contents.append(current_head.value) # append head value to list
            self.storage.move_to_end(current_head) # move head to tail
            num += 1 # record that iteration and repeat

        return list_buffer_contents

# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass
#
#     def append(self, item):
#         pass
#
#     def get(self):
#         pass

test = RingBuffer(3)
test.append('Josh')
test.append('Gabe')
test.append('Remy')
test.append('Jennifer')
print(test.get())