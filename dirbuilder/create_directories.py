import os
import argparse

def detect_indentation_size(lines):
    print("Detecting indentation size...")
    for line in lines:
        stripped_line = line.lstrip()
        if stripped_line != line:
            indentation = line[:line.index(stripped_line)]
            if "\t" in indentation:
                raise ValueError("Tabs are not allowed for indentation.")
            print(f"Detected indentation size: {len(indentation)}")
            return len(indentation)
    print("No indentation detected.")
    return 0

def get_current_path(stack, line, indentation_size):
    print(f"Processing line: {line}")
    level = int((len(line) - len(line.lstrip())) / indentation_size)
    while len(stack) > level + 1:
        print(f"Popping from stack: {stack[-1]}")
        stack.pop()
    current_path = os.path.join(stack[-1], line.strip())
    stack.append(current_path)
    print(f"Current path set to: {current_path}")
    return current_path, stack

def create_directory(dir_path):
    print(f"Creating directory: {dir_path}")
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def create_file(file_path):
    print(f"Creating file: {file_path}")
    if not os.path.exists(os.path.dirname(file_path)):
        print(f"Creating parent directory for the file: {os.path.dirname(file_path)}")
        os.makedirs(os.path.dirname(file_path))
    with open(file_path, 'w') as f:
        f.write("")

def create_directories_from_text(structured_tree, base_path):
    lines = [line for line in structured_tree.split('\n') if line.strip()]
    indentation_size = detect_indentation_size(lines)
    stack = [base_path]
    print(f"Initial base path: {base_path}")

    for line in lines:
        current_path, stack = get_current_path(stack, line, indentation_size)
        if line.endswith('/'):
            create_directory(current_path)
        else:
            create_file(current_path)

def main():
    parser = argparse.ArgumentParser(description="Convert a structured text file into a directory structure.")
    parser.add_argument("input_file", type=str, help="Path to the structured text file.")
    parser.add_argument("output_dir", type=str, help="Base path where the directory structure should be created.")
    
    args = parser.parse_args()
    print(f"Input file: {args.input_file}")
    print(f"Output directory: {args.output_dir}")

    with open(args.input_file, 'r') as f:
        structured_tree = f.read()

    print("Starting directory and file creation...")
    create_directories_from_text(structured_tree, args.output_dir)
    print("Creation process completed.")

if __name__ == "__main__":
    main()
