import random

class Node:
   
    def __init__(self, data=None):
        self.data = data
        self.next = None


    def __str__(self):
        return str(self.data)




class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0


    def __str__(self):
        
        if not self.head:
            return "[]"  

        nodes_str = []
        current_node = self.head
        
        while current_node:
            nodes_str.append(str(current_node.data))
            current_node = current_node.next
        return "[" + ", ".join(nodes_str) + "]"


    def __len__(self):
        return self._size


    def is_empty(self):
        return self.head is None


    def _create_node(self, value):
        return value if isinstance(value, Node) else Node(value)


    def add_to_beginning(self, value):
        new_node = self._create_node(value)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1


    def append(self, value):
        new_node = self._create_node(value)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1


    def add_before(self, target_value, value):
        
        if self.is_empty():
            print(f"Список порожній, неможливо додати {value} перед {target_value}.")
            return False

        new_node = self._create_node(value)

        if self.head.data == target_value:
            new_node.next = self.head
            self.head = new_node
            self._size += 1
            return True
        else:
            current_node = self.head
            
            while current_node.next and current_node.next.data != target_value:
                current_node = current_node.next

            if current_node.next:
                new_node.next = current_node.next
                current_node.next = new_node
                self._size += 1
                return True
            else:
                print(f"Цільове значення {target_value} не знайдено в списку.")
                return False


    def add_after(self, target_value, value):
       
        if self.is_empty():
            print(f"Список порожній, неможливо додати {value} після {target_value}.")
            return False

        new_node = self._create_node(value)
        current_node = self.head

        while current_node and current_node.data != target_value:
            current_node = current_node.next

        if current_node:
            new_node.next = current_node.next
            current_node.next = new_node
            self._size += 1
            if new_node.next is None:
                self.tail = new_node
            return True
        else:
            print(f"Цільове значення {target_value} не знайдено в списку.")
            return False


    def remove_first(self):

        if self.is_empty():
            return None # Можна викликати IndexError("List is empty")

        data = self.head.data
        self.head = self.head.next
        self._size -= 1

        if self.head is None:
            self.tail = None
        return data


    def remove_last(self):
        
        if self.is_empty():
            return None

        data = self.tail.data 

        if self._size == 1:
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            
            while current_node.next != self.tail:
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node
        self._size -= 1
        return data


    def get_at_index(self, index):
       
        if not (0 <= index < self._size):
            raise IndexError(f"Index {index} out of bounds for size {self._size}")

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.data


    def find(self, value):
        
        current_node = self.head
        index = 0
        
        while current_node:
            if current_node.data == value:
                return index
            current_node = current_node.next
            index += 1
        return -1


    def insert_at_index(self, index, value):
        
        if not (0 <= index <= self._size):
            raise IndexError(f"Index {index} out of bounds for size {self._size}")

        if index == 0:
            self.add_to_beginning(value)
            return
        if index == self._size:
            self.append(value)
            return

        new_node = self._create_node(value)
        current_node = self.head
        
        for _ in range(index - 1):
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node
        self._size += 1


    def remove_at_index(self, index):
        
        if not (0 <= index < self._size):
            raise IndexError(f"Index {index} out of bounds for size {self._size}")

        if index == 0:
            return self.remove_first()
        if index == self._size - 1:
            return self.remove_last()

        current_node = self.head
        
        for _ in range(index - 1):
            current_node = current_node.next

        removed_node = current_node.next
        data = removed_node.data
        current_node.next = removed_node.next
        self._size -= 1
        return data


    def insertion_sort(self):
        
        if self._size <= 1:
            return # або return(self) якщо треба забезпечити повернення списку

        sorted_list = LinkedList() 
        current_node = self.head

        while current_node:
            next_node = current_node.next

            if sorted_list.is_empty() or current_node.data < sorted_list.head.data:
                current_node.next = sorted_list.head
                sorted_list.head = current_node
                if sorted_list.tail is None:
                    sorted_list.tail = current_node
            else:
                temp_sorted = sorted_list.head
                while temp_sorted.next and temp_sorted.next.data < current_node.data:
                    temp_sorted = temp_sorted.next
                current_node.next = temp_sorted.next
                temp_sorted.next = current_node
                if current_node.next is None:
                    sorted_list.tail = current_node

            current_node = next_node

        # Оновлюємо поточний список відсортованим
        self.head = sorted_list.head
        self.tail = sorted_list.tail
        # або закоментовуємо попередні дві строки та return sorted_list, якщо треба забезпечити повернення списку


    def merge_sort(self):
        
        self.head = self._merge_sort_recursive(self.head)
        current = self.head
        
        if current:
            while current.next:
                current = current.next
            self.tail = current
        else:
            self.tail = None


    def _merge_sort_recursive(self, head_node):
        
        if head_node is None or head_node.next is None:
            return head_node 

        # Ділимо список на дві половини
        middle = self._get_middle(head_node)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort_recursive(head_node)
        right = self._merge_sort_recursive(next_to_middle)

        # Злиття відсортованих половин
        sorted_head = self._merge_lists(left, right)
        return sorted_head


    def _get_middle(self, head_node):
        
        if head_node is None:
            return head_node

        left_iterator = head_node
        right_iterator = head_node

        while right_iterator.next and right_iterator.next.next:
            left_iterator = left_iterator.next
            right_iterator = right_iterator.next.next
        return left_iterator


    def _merge_lists(self, list_left, list_right):
        
        if list_left is None:
            return list_right
        if list_right is None:
            return list_left

        if list_left.data < list_right.data:
            result = list_left
            list_left = list_left.next
        else:
            result = list_right
            list_right = list_right.next

        current = result
        while list_left and list_right:
            if list_left.data < list_right.data:
                current.next = list_left
                list_left = list_left.next
            else:
                current.next = list_right
                list_right = list_right.next
            current = current.next

        if list_left:
            current.next = list_left
        if list_right:
            current.next = list_right

        return result




if __name__ == '__main__':

    llist = LinkedList()

    for _ in range(5):
        llist.add_to_beginning(random.randint(1, 100))
    print(f"Список після додавання на початок: {llist}")
    print(f"Розмір списку: {len(llist)}")
    print(f"Голова: {llist.head}, Хвіст: {llist.tail}")

    for _ in range(5):
        llist.append(random.randint(1, 100))
    print(f"Список після додавання в кінець: {llist}")
    print(f"Розмір списку: {len(llist)}")

    llist.insert_at_index(0, 0)
    print(f"Після вставки 0 на індекс 0: {llist}")

    llist.insert_at_index(len(llist), 999)
    print(f"Після вставки 999 на останній індекс: {llist}")

    if len(llist) >= 3:
        llist.insert_at_index(2, 555) 
        print(f"Після вставки 555 на індекс 2: {llist}")

    try:
        llist.insert_at_index(len(llist) + 1, 111) 
    except IndexError as e:
        print(f"Очікувана помилка: {e}")

    if not llist.is_empty():
        removed_val = llist.remove_at_index(0)
        print(f"Видалили {removed_val} з індексу 0. Список: {llist}")

    if not llist.is_empty():
        removed_val = llist.remove_at_index(len(llist) - 1)
        print(f"Видалили {removed_val} з останнього індексу. Список: {llist}")
        print(f"Розмір: {len(llist)}, Голова: {llist.head}, Хвіст: {llist.tail}")

    if len(llist) >= 3:
        removed_val = llist.remove_at_index(1)
        print(f"Видалили {removed_val} з індексу 1. Список: {llist}")
        print(f"Розмір: {len(llist)}, Голова: {llist.head}, Хвіст: {llist.tail}")

    try:
        if not llist.is_empty():
            llist.remove_at_index(len(llist))
    except IndexError as e:
        print(f"Очікувана помилка: {e}")

    new_llist = LinkedList()
    new_llist.append(10)
    new_llist.append(20)
    new_llist.append(30)
    print(f"Оригінальний список: {new_llist}")

    new_llist.add_before(20, 15) 
    print(f"Після add_before(20, 15): {new_llist}")

    new_llist.add_before(10, 5)
    print(f"Після add_before(10, 5): {new_llist}") 

    new_llist.add_before(99, 100) 
    print(f"Після add_before(99, 100): {new_llist}")

    new_llist.add_after(20, 25)
    print(f"Після add_after(20, 25): {new_llist}") 

    new_llist.add_after(30, 35)
    print(f"Після add_after(30, 35): {new_llist}")
    print(f"Хвіст: {new_llist.tail}")

    new_llist.add_after(99, 100) 
    print(f"Після add_after(99, 100): {new_llist}")


    print(f"Список: {new_llist}")
    print(f"Індекс 15: {new_llist.find(15)}")
    print(f"Індекс 5: {new_llist.find(5)}")
    print(f"Індекс 35: {new_llist.find(35)}")
    print(f"Індекс 100: {new_llist.find(100)}")

    insertion_list = LinkedList()
    for _ in range(15):
        insertion_list.append(random.randint(1, 100))
    print(f"Оригінальний список: {insertion_list}")
    insertion_list.insertion_sort()
    print(f"Відсортований список (вставка): {insertion_list}")

    merge_list = LinkedList()
    for _ in range(12):
        merge_list.append(random.randint(1, 100))
    print(f"Оригінальний список: {merge_list}")
    merge_list.merge_sort()
    print(f"Відсортований список (злиття): {merge_list}")