import uuid
import heapq
import random
import networkx as nx
import matplotlib.pyplot as plt


class Node:
  def __init__(self, key, color_to_set=(0.0, 0.0, 0.3)):
    self.left = None
    self.right = None
    self.val = key
    self.color = color_to_set # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


  def set_color(self, new_color):
    
        if isinstance(new_color, tuple) and len(new_color) == 3 and all(0.0 <= c <= 1.0 for c in new_color):
            self.color = new_color
        else:
            print(f"Невірний формат кольору: {new_color}")


  def get_color(self):
        return self._visual_color


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
    if node.left:
      graph.add_edge(node.id, node.left.id)
      l = x - 1 / 2 ** layer
      pos[node.left.id] = (l, y - 1)
      l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph


def draw_tree(tree_root):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  colors = [node[1]['color'] for node in tree.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

  plt.figure(figsize=(10, 10))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()


# Створення дерева
# root = Node(0)
# root.left = Node(4)
# root.left.left = Node(5)
# root.left.right = Node(10)
# root.right = Node(1)
# root.right.left = Node(3)

def generate_random_heap(length = 30):
    heap_list = []
    
    for _ in range(0, length):
        heap_list.append(random.randint(0, 100))
        
    heapq.heapify(heap_list)
    return heap_list


def generate_heap_tree(heap: list) -> Node:
    root = Node(heap[0])
    dict_nodes = {0: root}
    length = len(heap)
    
    for i in range(0, length // 2):
        node_left = None if (2 * i + 1) > (length - 1) else Node(heap[2 * i + 1]) 
        node_right = None if (2 * i + 2) > (length - 1) else Node(heap[2 * i + 2])
        current_node = dict_nodes.get(i)
        current_node.left = node_left
        current_node.right = node_right
        if node_left is not None:
            dict_nodes[(2 * i + 1)] = node_left
        if node_right is not None:   
            dict_nodes[(2 * i + 2)] = node_right
            
    return root



if __name__ == '__main__':
    
    heap = generate_random_heap(40)
    root = generate_heap_tree(heap)

    # Відображення дерева
    draw_tree(root)