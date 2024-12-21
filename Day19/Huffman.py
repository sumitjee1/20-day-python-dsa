#Code to impliment Huffman Coding(Greedy Algorithm)
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def build_huffman_tree(char_freq):
    nodes = [Node(char, freq) for char, freq in char_freq.items()]

    while len(nodes) > 1:

        nodes = sorted(nodes, key=lambda x: x.freq)

        left = nodes.pop(0)
        right = nodes.pop(0)

        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right

        
        nodes.append(new_node)

    return nodes[0]  

def generate_codes(node, current_code="", code_dict={}):
    if node is None:
        return

    if node.char is not None:
        code_dict[node.char] = current_code

    generate_codes(node.left, current_code + "0", code_dict)
    generate_codes(node.right, current_code + "1", code_dict)

    return code_dict

if __name__ == "__main__":
    char_freq = {
        'A': 5,
        'B': 9,
        'C': 12,
        'D': 13,
        'E': 16,
        'F': 45
    }
    huffman_tree = build_huffman_tree(char_freq)
    huffman_codes = generate_codes(huffman_tree)
    print("Huffman Codes for each character:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")
