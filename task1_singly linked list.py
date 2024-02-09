class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    # def search_element(self, data: int) -> Node | None:
    #     cur = self.head
    #     while cur:
    #         if cur.data == data:
    #             return cur
    #         cur = cur.next
    #     return None

    def print_list(self):
        current = self.head
        while current:
          print(current.data)
          current = current.next

    def reverse_linked_list(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        sorted_tail = self.head
        while sorted_tail.next:
            curr = sorted_tail.next
            if curr.data < self.head.data:
                sorted_tail.next = curr.next
                curr.next = self.head
                self.head = curr
            else:
                prev = self.head
                while prev != sorted_tail and prev.next.data < curr.data:
                    prev = prev.next
                if prev == sorted_tail:
                    sorted_tail = sorted_tail.next
                else:
                    sorted_tail.next = curr.next
                    curr.next = prev.next
                    prev.next = curr

    @staticmethod
    def merge_sorted_lists(head1, head2):
        # Створення фіктивного початкового вузла, який спростить об'єднання списків
        dummy = Node()
        tail = dummy
        
        while head1 and head2:
            # Вибір вузла з меншим значенням
            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        
        # Додавання залишків від одного зі списків, якщо вони є
        if head1:
            tail.next = head1
        elif head2:
            tail.next = head2
        
        return dummy.next
    

llist = LinkedList()
llist2 = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(1)
llist.insert_at_beginning(24)
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

llist2.insert_at_beginning(4)
llist2.insert_at_beginning(21)
llist2.insert_at_beginning(8)
llist2.insert_at_beginning(11)
llist2.insert_at_beginning(15)
llist2.insertion_sort()


# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

# # Пошук елемента у зв'язному списку
# print("\nШукаємо елемент 15:")
# element = llist.search_element(15)
# if element:
#   print(element.data)

print("\n")

llist.reverse_linked_list()

print("Реверсований список:")
llist.print_list()
print("\n")

print("Відсортований список:")
llist.insertion_sort()
llist.print_list()
print("\n")

new_head = LinkedList.merge_sorted_lists(llist.head, llist2.head)

current = new_head
print("Об'єднанні відсортовані списки:")
while current:
    print(current.data, end=' ')
    current = current.next
print("\n")