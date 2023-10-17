import os
import shutil
from dirbuilder.create_directories import generate_directory_structure, create_directories_from_text
import dirbuilder.interface as interface

test_root_path = "test_root"

def setup_module(module):
    os.makedirs(test_root_path, exist_ok=True)

def teardown_module(module):
    if os.path.exists(test_root_path):
        shutil.rmtree(test_root_path)


def test_simple_directory_creation(mocker):
    mocker.patch.object(interface, 'generate_directory_structure', return_value="""
    root/
        test_dir/
            test_subdir/
                test_file.txt
    """)
    create_directories_from_text(generate_directory_structure(""), test_root_path)
    assert os.path.exists(os.path.join(test_root_path, "root", "test_dir"))
    assert os.path.exists(os.path.join(test_root_path, "root", "test_dir", "test_subdir"))
    assert os.path.isfile(os.path.join(test_root_path, "root", "test_dir", "test_subdir", "test_file.txt"))

def test_multiple_directories_files_creation(mocker):
    mocker.patch.object(interface, 'generate_directory_structure', return_value="""
    root/
        dir1/
            file1.py
            file2.py
        dir2/
            file3.py
    """)
    create_directories_from_text(generate_directory_structure(""), test_root_path)
    assert os.path.exists(os.path.join(test_root_path, "root", "dir1"))
    assert os.path.isfile(os.path.join(test_root_path, "root", "dir1", "file1.py"))
    assert os.path.isfile(os.path.join(test_root_path, "root", "dir1", "file2.py"))
    assert os.path.exists(os.path.join(test_root_path, "root", "dir2"))
    assert os.path.isfile(os.path.join(test_root_path, "root", "dir2", "file3.py"))

def test_directory_overwriting(mocker):
    existing_path = os.path.join(test_root_path, "root", "existing_dir")
    os.makedirs(existing_path, exist_ok=True)

    with open(os.path.join(existing_path, "existing_file.txt"), "w") as f:
        f.write("Existing content")

    mocker.patch.object(interface, 'generate_directory_structure', return_value="""
    root/
        existing_dir/
            new_file.py
    """)
    create_directories_from_text(generate_directory_structure(""), test_root_path)
    assert os.path.exists(existing_path)
    assert not os.path.isfile(os.path.join(existing_path, "existing_file.txt"))  # Ensure the file was not overwritten
    assert os.path.isfile(os.path.join(existing_path, "new_file.py"))

def test_root_only_directory_creation(mocker):
    mocker.patch.object(interface, 'generate_directory_structure', return_value="""
    root_dir/
    """)
    create_directories_from_text(generate_directory_structure(""), test_root_path)
    assert os.path.exists(os.path.join(test_root_path, "root_dir"))

def test_root_only_file_creation(mocker):
    mocker.patch.object(interface, 'generate_directory_structure', return_value="""
    root_file.txt
    """)
    create_directories_from_text(generate_directory_structure(""), test_root_path)
    assert os.path.isfile(os.path.join(test_root_path, "root_file.txt"))

def test_ellipsis_handling(mocker):
    mocker.patch.object(interface, 'generate_directory_structure', return_value="""
    root/
        test_dir/
            ...
            test_subdir/
                test_file.txt
    """)
    create_directories_from_text(generate_directory_structure(""), test_root_path)

    assert os.path.exists(os.path.join(test_root_path, "root", "test_dir"))
    assert not os.path.exists(os.path.join(test_root_path, "root", "test_dir", "..."))  # Ensure ... directory doesn't exist
    assert os.path.exists(os.path.join(test_root_path, "root", "test_dir", "test_subdir"))
    assert os.path.isfile(os.path.join(test_root_path, "root", "test_dir", "test_subdir", "test_file.txt"))
