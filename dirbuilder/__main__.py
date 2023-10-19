from .interface import generate_directory_structure
from .create_directories import create_directories_from_text
import logging
import argparse

def main():
    parser = argparse.ArgumentParser(description='Directory Builder Tool')
    parser.add_argument('input_file_path', help='Path to the input file containing the directory structure in plain text.')
    parser.add_argument('output_directory_path', help='Path where the directories and files will be created.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()

    # Set logging level
    logging_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=logging_level, format="%(asctime)s - %(levelname)s - %(message)s")

    with open(args.input_file_path, 'r') as f:
        plain_text_tree = f.read()

    # Using OpenAI to get the structured directory format
    directory_structure = generate_directory_structure(plain_text_tree)

    # Using the provided function to create the directories and files
    create_directories_from_text(directory_structure, args.output_directory_path)

if __name__ == '__main__':
    main()
