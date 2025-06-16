from collections import deque
from heap_visualization import *


def calculate_rgb_color(start_rgb, end_rgb, delta):

    r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * delta)
    g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * delta)
    b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * delta)
    return (r, g, b)


def depth_first_search(root: Node):
    if not root:
        return

    visited = set()
    stack = [root]
    ordered_nodes = []

    while stack:
        current_node = stack.pop() 

        if current_node not in visited:
            visited.add(current_node)
            ordered_nodes.append(current_node)

            if current_node.right is not None:

                if current_node.right not in visited:
                    stack.append(current_node.right)

            if current_node.left is not None:

                if current_node.left not in visited:
                    stack.append(current_node.left)

    colorize_nodes(ordered_nodes)


def colorize_nodes(nodes_list: list):
    total_nodes = len(nodes_list)

    start_color_rgb = (0, 50, 0) 
    end_color_rgb = (125, 255, 100)

    for i, node in enumerate(nodes_list):
        delta = i / (total_nodes - 1) if total_nodes > 1 else 0.0

        calculated_rgb = calculate_rgb_color(start_color_rgb, end_color_rgb, delta)

        final_color = (calculated_rgb[0] / 255.0, calculated_rgb[1] / 255.0, calculated_rgb[2] / 255.0)

        node.set_color(final_color) 



def breadth_first_search(root: Node):
    if not root:
        return

    visited = set()
    queue = deque([root])
    ordered_nodes = []

    while queue:
        current_node = queue.popleft()

        if current_node not in visited:
            visited.add(current_node)
            ordered_nodes.append(current_node)

            if current_node.left is not None:

                if current_node.left not in visited:
                    queue.extend([current_node.left])

            if current_node.right is not None:

                if current_node.right not in visited:
                    queue.extend([current_node.right])

    colorize_nodes(ordered_nodes)



if __name__ == '__main__':

    initial_heap = generate_random_heap(20)
    heapq.heapify(initial_heap)
    root = generate_heap_tree(initial_heap)

    depth_first_search(root)

    draw_tree(root)


    breadth_first_search(root)

    draw_tree(root)