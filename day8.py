'''
https://adventofcode.com/2018/day/8

Input: https://adventofcode.com/2018/day/8/input

cat inputs/day8.txt | python3 day8.py
'''


class Node:

    def __init__(self, position):
        self.position = position
        #self.end_position = 0

        self.meta_count = 0
        self.nodes_count = 0

        self.meta = []
        self.nodes = []

        #self.parent = None


l = list(map(int, input().split()))


def complete_node(node):
    node.nodes_count = l[node.position]
    node.meta_count = l[node.position + 1]
    current_index = node.position + 2
    for _ in range(node.nodes_count):
        new_node = Node(current_index)
        current_index = complete_node(new_node) + 1
        node.nodes.append(new_node)
    for _ in range(node.meta_count):
        node.meta.append(l[current_index])
        current_index += 1
    #node.end_position = current_index - 1
    return current_index - 1


root = Node(0)

complete_node(root) # finished constructing the tree


def sum_meta(node):
    s = sum(node.meta)
    for n in node.nodes:
        s += sum_meta(n)
    return s

print(sum_meta(root))
