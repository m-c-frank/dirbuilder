from dirbuilder.interface import generate_directory_structure
import os

def create_directories_from_text(structured_text, root_path):
    lines = structured_text.strip().split('\n')
    for line in lines:
        path = os.path.join(root_path, line.strip())
        if path.endswith('/'):
            os.makedirs(path, exist_ok=True)
        else:
            dir_path = os.path.dirname(path)
            os.makedirs(dir_path, exist_ok=True)
            with open(path, 'w') as f:
                f.write('')  # Create an empty file

# Example plain-text tree structure
plain_text_tree = """
conceptsplitter/
-> conceptsplitter/
-> -> __init__.py
-> -> split_concepts.py
-> -> interface.py
-> -> utils.py
-> tests/
-> -> __init__.py
-> -> test_split_concepts.py
-> -> test_utils.py
-> .gitignore
-> README.md
-> requirements.txt
-> setup.py
"""

structured_tree = generate_directory_structure(plain_text_tree)
print(structured_tree)
