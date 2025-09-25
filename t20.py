import heapq
import pickle
import os

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

def build_huffman_tree(freq):
    heap = [Node(ch, f) for ch, f in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        merged = Node(None, n1.freq + n2.freq)
        merged.left, merged.right = n1, n2
        heapq.heappush(heap, merged)
    return heap[0]

def build_codes(root):
    codes = {}
    def traverse(node, path=""):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = path
        traverse(node.left, path + "0")
        traverse(node.right, path + "1")
    traverse(root)
    return codes

def compress_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    if not text:
        print("Input file is empty!")
        return 0

    freq = build_frequency(text)
    root = build_huffman_tree(freq)
    codes = build_codes(root)

    encoded_text = "".join(codes[ch] for ch in text)

    extra_padding = (8 - len(encoded_text) % 8) % 8
    padded_info = "{0:08b}".format(extra_padding)
    encoded_text = padded_info + encoded_text + "0" * extra_padding

    b = bytearray()
    for i in range(0, len(encoded_text), 8):
        b.append(int(encoded_text[i:i+8], 2))

    with open("compressed.bin", "wb") as f:
        f.write(bytes(b))
    with open("codes.pkl", "wb") as f:
        pickle.dump(codes, f)

    ratio = os.path.getsize("compressed.bin") / os.path.getsize(file_path)
    print("Compression done. Ratio:", ratio)
    return ratio

def decompress_text(file_path):
    with open("codes.pkl", "rb") as f:
        codes = pickle.load(f)
    reverse_codes = {v: k for k, v in codes.items()}

    bit_string = ""
    with open(file_path, "rb") as f:
        byte = f.read(1)
        while byte:
            byte = byte[0]
            bit_string += bin(byte)[2:].rjust(8, "0")
            byte = f.read(1)

    extra_padding = int(bit_string[:8], 2)
    bit_string = bit_string[8:-extra_padding] if extra_padding > 0 else bit_string[8:]

    decoded_text = ""
    current_code = ""
    for bit in bit_string:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""

    with open("decompressed.txt", "w", encoding="utf-8") as f:
        f.write(decoded_text)
    print("Decompression done. File: decompressed.txt")
    return "decompressed.txt"

# ---------------- Example ----------------
if __name__ == "__main__":
    compress_text("input.txt")
    decompress_text("compressed.bin")
