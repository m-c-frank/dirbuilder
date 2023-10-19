import os
import logging

def detect_indentation_size(lines):
    logging.debug("Detecting indentation size...")
    
    for line in lines:
        stripped_line = line.lstrip()
        if stripped_line != line:
            indentation = line[:line.index(stripped_line)]
            if "\t" in indentation:
                raise ValueError("Tabs are not allowed for indentation.")
            logging.debug(f"Detected indentation size: {len(indentation)}")
            return len(indentation)
    
    logging.warning("No indentation detected.")
    return 0

def get_current_path(stack, line, indentation_size):
    logging.debug(f"Processing line: {line}")
    
    level = int((len(line) - len(line.lstrip())) / indentation_size)
    while len(stack) > level + 1:
        logging.debug(f"Popping from stack: {stack[-1]}")
        stack.pop()
    current_path = os.path.join(stack[-1], line.strip())
    stack.append(current_path)
    
    logging.debug(f"Current path set to: {current_path}")
    return current_path, stack

def create_directory(dir_path):
    logging.debug(f"Creating directory: {dir_path}")
    
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def create_file(file_path):
    logging.debug(f"Creating file: {file_path}")
    
    if not os.path.exists(os.path.dirname(file_path)):
        logging.debug(f"Creating parent directory for the file: {os.path.dirname(file_path)}")
        os.makedirs(os.path.dirname(file_path))
    
    with open(file_path, 'w') as f:
        f.write("")

def create_directories_from_text(structured_tree, base_path):
    lines = [line for line in structured_tree.split('\n') if line.strip()]
    indentation_size = detect_indentation_size(lines)
    stack = [base_path]
    logging.info(f"Initial base path: {base_path}")

    for line in lines:
        current_path, stack = get_current_path(stack, line, indentation_size)
        if line.endswith('/'):
            create_directory(current_path)
        else:
            create_file(current_path)
        # Compare expected directory or file creation with the actual result and log discrepancies
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            if line.endswith('/') and not os.path.isdir(current_path):
                logging.debug(f"Expected to create directory: {current_path} but failed.")
            elif not line.endswith('/') and not os.path.isfile(current_path):
                logging.debug(f"Expected to create file: {current_path} but failed.")
