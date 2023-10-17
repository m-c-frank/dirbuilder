# dirbuilder

`dirbuilder` is a versatile utility that translates a structured text representation into a real-world directory structure. If you're conceptualizing a new project, organizing a set of files, or laying out a precise folder hierarchy, `dirbuilder` simplifies the task, turning your text depiction into an actual directory structure.

## Features

- Convert a textual representation into directories and files.
- Auto-detects indentation to discern directory levels.
- Allows for simultaneous directory and file creation from the text blueprint.
- Gracefully manages spaces and nested hierarchies.
- User-friendly command-line interface.

## Directory Structure

```bash
.
├── LICENCE.md
├── README.md
├── __pycache__
│   ├── various cached files
├── dirbuilder
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── various cached files
│   ├── create_directories.py
│   └── interface.py
├── setup.py
├── tests
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── various cached files
│   ├── test_create_directories.py
│   └── test_interface.py
└── uniformatter.ppt
```

## Setup

1. Clone the repository:

    ```bash
    git clone [repository_url]
    cd dirbuilder
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Create a structured text file that mirrors your desired directory layout. Designate directories with a `/` at the end, and use indentation to indicate nesting. Here's an example:

    ```
    project/
      images/
      README.md
    ```

2. Run the `dirbuilder` script:

   ```bash
   python -m dirbuilder [input_file_path] [output_directory_path]
   ```

Using the example above, a `project` directory will be made, containing an `images` subdirectory and a `README.md` file.

## Related Tools

<!--START_TOKEN-->
**Note Utilities Ecosystem**: A suite of tools designed to streamline and enhance your note-taking and information processing workflows.

- **[workflowlibrary](https://github.com/m-c-frank/workflowlibrary)** - Centralizes and synchronizes the "Related Tools" section across the ecosystem.
- **[noteutilsyncer](https://github.com/m-c-frank/noteutilsyncer)** - A centralized tool that automates the synchronization of the "Related Tools" section across READMEs in the noteutils ecosystem.
- **[conceptsplitter](https://github.com/m-c-frank/conceptsplitter)** - Extract atomic concepts from a given text using the OpenAI API.
- **[textdownloader](https://github.com/m-c-frank/textdownloader)** - A browser extension to automatically generate text dumps for processing.
<!--END_TOKEN-->

## Contributing

Contributions to the dirbuilder project or the note utilities ecosystem are welcome. If you have ideas for improvements or new features, please feel free to submit issues, suggestions, or pull requests in this repository or contact me!

## License

The dirbuilder project is open-source and licensed under the [GOS License](https://github.com/m-c-frank/textdownloader/blob/main/LICENCE.md).

## Credits

The dirbuidlder project is developed and maintained by [Martin Christoph Frank](https://github.com/m-c-frank). If you have any questions or need assistance, please contact [martin7.frank7@gmail.com](martin7.frank7@gmail.com).