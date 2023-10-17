import os

def detect_indentation_size(lines):
    # Detect the first indented line
    for line in lines:
        stripped_line = line.lstrip()
        if stripped_line != line:
            # Determine the indentation
            indentation = line[:line.index(stripped_line)]
            if "\t" in indentation:
                raise ValueError("Tabs are not allowed for indentation.")
            return len(indentation)
    return 0

def get_current_path(stack, line, indentation_size):
    level = int((len(line) - len(line.lstrip())) / indentation_size)
    while len(stack) > level + 1:
        stack.pop()
    current_path = os.path.join(stack[-1], line.strip())
    stack.append(current_path)
    return current_path, stack


def create_directory(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def create_file(file_path):
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    with open(file_path, 'w') as f:
        f.write("")

def create_directories_from_text(structured_tree, base_path):
    lines = [line for line in structured_tree.split('\n') if line.strip()]
    indentation_size = detect_indentation_size(lines)
    stack = [base_path]

    for line in lines:
        current_path, stack = get_current_path(stack, line, indentation_size)
        if line.endswith('/'):
            create_directory(current_path)
        else:
            create_file(current_path)
