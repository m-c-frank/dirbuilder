# dirbuilder

`dirbuilder` is a tool that effortlessly translates a structured text representation into an actual directory structure, streamlining the process of laying out projects, organizing files, and creating folder hierarchies. 

## Features

- Transforms textual representations into directories and files.
- Intelligently detects indentation to decipher directory levels.
- Allows for the simultaneous creation of directories and files from text blueprints.
- Handles spaces and nested hierarchies with ease.
- Provides a simple command-line interface.

## Directory Structure

```bash
.
├── LICENCE.md
├── README.md
├── dirbuilder
│   ├── __init__.py
│   ├── __main__.py
│   ├── create_directories.py
│   ├── interface.py
│   └── uniformatter.ppt
├── requirements.txt
├── setup.py
└── tests
    ├── __init__.py
    ├── test_create_directories.py
    └── test_interface.py
```

## Installation

To install `dirbuilder`, simply use pip:

```bash
pip install dirbuilder
```

You can also install the latest version directly from the repository:

```bash
pip install git+https://github.com/m-c-frank/dirbuilder.git
```

## Usage

1. Draft a structured text file reflecting your desired directory layout. Mark directories with a `/` at the end and use indentation to signify nesting:

```bash
project/
    images/
        README.md
```

2. Use the `dirbuilder` tool:

```bash
dirbuilder [input_file_path] [output_directory_path]
```

This command will create a `project` directory containing an `images` subdirectory and a `README.md` file inside it.

## Related Tools

<!--START_TOKEN-->
**Note Utilities Ecosystem**: A suite of tools designed to streamline and enhance your note-taking and information processing workflows.

- **[dirbuilder](https://github.com/m-c-frank/dirbuilder)** - Builds a directory structure from `tree`
- **[workflowlibrary](https://github.com/m-c-frank/workflowlibrary)** - Centralizes and synchronizes the "Related Tools" section across the ecosystem.
- **[noteutilsyncer](https://github.com/m-c-frank/noteutilsyncer)** - A centralized tool that automates the synchronization of the "Related Tools" section across READMEs in the noteutils ecosystem.
- **[conceptsplitter](https://github.com/m-c-frank/conceptsplitter)** - Extract atomic concepts from a given text using the OpenAI API.
- **[textdownloader](https://github.com/m-c-frank/textdownloader)** - A browser extension to automatically generate text dumps for processing.
- **[contenttree](https://github.com/m-c-frank/contenttree)** - A utility to print a repository's tree structure and file content
<!--END_TOKEN-->

## Contributing

If you're interested in contributing to `dirbuilder` or the larger Note Utilities ecosystem, we're eager to collaborate. Raise issues, suggest enhancements, or submit pull requests. Feel free to reach out directly with any inquiries!

## License

`dirbuilder` is an open-source endeavor licensed under the [GOS License](https://github.com/m-c-frank/dirbuilder/blob/main/LICENCE.md).

## Credits

`dirbuilder` was developed and is maintained by [Martin Christoph Frank](https://github.com/m-c-frank). For questions or assistance, please email [martin7.frank7@gmail.com](martin7.frank7@gmail.com).
