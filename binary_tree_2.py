class BinaryTreeNode:
    def __init__(self, value, parent=None):
        self.left = None  # ссылка на левый дочерний узел
        self.right = None  # ссылка на правый дочерний узел
        self.parent = parent  # ссылка на родителя
        self.value = value  # полезная нагрузка

    def find_node(self, value):
        node = self
        while node:
            if value == node.value:
                return node
            if value < node.value:
                node = node.left
            if value > node.value:
                node = node.right
        return None

    def insert_node(self, value):
        return self._insert_node(value, self)

    def _insert_node(self, value, parent_node):
        if value < parent_node.value:
            if parent_node.left is None:
                parent_node.left = BinaryTreeNode(value, parent_node)
            else:
                self._insert_node(value, parent_node.left)
        elif value > parent_node.value:
            if parent_node.right is None:
                parent_node.right = BinaryTreeNode(value, parent_node)
            else:
                self._insert_node(value, parent_node.right)

    def remove_node(self, value):
        return self._remove_node(value, self)

    def _remove_node(self, value, node):
        if node is None:
            return None

        if value < node.value:
            node.left = self._remove_node(value, node.left)
            return node
        elif value > node.value:
            node.right = self._remove_node(value, node.right)
            return node
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                original = node
                node = node.right
                while node.left:
                    node = node.left
                node.right = self._remove_node(node.value, original.right)
                node.left = original.left
                return node

    def traverse_recursive(self):
        if self is not None:
            print(f"node = {self.value}")
            if self.left is not None:
                self.left.traverse_recursive()
            if self.right is not None:
                self.right.traverse_recursive()

    def traverse_with_stack(self):
        stack = []
        stack.append(self)
        while len(stack) > 0:
            current_node = stack.pop()
            print(f"node = {current_node.value}")
            if current_node.right is not None:
                stack.append(current_node.right)
            if current_node.left is not None:
                stack.append(current_node.left)

    def traverse_with_queue(self):
        queue = []
        queue.append(self)
        while len(queue) > 0:
            current_node = queue.pop(0)
            print(f"node = {current_node.value}")
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)


# Создаем экземпляр класса BinaryTreeNode
node = BinaryTreeNode(5)

# Вызываем методы на созданном экземпляре
node.insert_node(3)
node.insert_node(7)
node.insert_node(4)
node.insert_node(6)

# Удаляем узел со значением 4
node.remove_node(4)

print("Используем метод traverse_recursive: ")
node.traverse_recursive()
print("Используем метод traverse_with_stack: ")
node.traverse_with_stack()
