import openai
import os
import re
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the OpenAI API key from environment variable
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("Please set the OPENAI_API_KEY in the .env file.")
openai.api_key = API_KEY

SYSTEM_MESSAGE = """
You are equipped with the capability to comprehend directory structure instructions given in plain text. Based on the text provided, you must determine the hierarchical directory structure and generate the appropriate structure format. Use the established standards to delineate directories and files, ensuring clarity in the representation.
"""

def get_structure_representation(prompt):
    """Fetch the directory structure representation from OpenAI API based on the provided instruction."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": prompt},
         ]
    )
    return response.choices[0]["message"]["content"]

def generate_directory_structure(plain_text_tree, template_filename="uniformatter.ppt"):
    """
    Generate a directory structure based on the given instruction using a template and the OpenAI API.
    
    Args:
    - input_instruction (str): The plain text tree for the directory structure.
    - template_filename (str): Filename of the template used for the generation.
    
    Returns:
    - str: A string representing the generated directory structure.
    """
    
    with open(template_filename, "r") as file:
        template = file.read()
    
    # Embed the input instruction into the template
    prompt = template.replace("<DIRECTORY_STRUCTURE_TEXT_DUMP", plain_text_tree)
    
    directory_representation = get_structure_representation(prompt)

    return directory_representation
