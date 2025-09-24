import re

def tokenize_text(file_path, delimiters=r"[\s,;.!?-]"):
    with open(file_path, "r") as f:
        text = f.read()
    tokens = re.findall(r"\w+|[" + delimiters.strip("[]") + "]", text)
    return [t for t in tokens if t.strip()]
tokens = tokenize_text("input.txt")
print(tokens)
