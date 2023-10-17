import pytest
from dirbuilder.create_directories import (
    detect_indentation_size,
    get_current_path,
    create_directory,
    create_file,
    create_directories_from_text
)
import os

def test_detect_indentation_size():
    lines = ["root/", "    dir1/"]
    assert detect_indentation_size(lines) == 4

    lines = ["root/", "\tdir1/"]
    with pytest.raises(ValueError):
        detect_indentation_size(lines)

    # Test with no indentation
    lines = ["root/"]
    assert detect_indentation_size(lines) == 0

def test_get_current_path():
    stack = ["/root_path"]
    line = "    dir1/"
    path, updated_stack = get_current_path(stack, line, 4)
    assert path == os.path.join("/root_path", "dir1/")
    assert updated_stack == ["/root_path", os.path.join("/root_path", "dir1/")]

def test_create_directory(tmp_path):
    dir_path = os.path.join(tmp_path, "new_dir")
    create_directory(dir_path)
    assert os.path.isdir(dir_path)

    # Given the function's idempotent behavior, it should not raise an error if the directory already exists.
    create_directory(dir_path)
    assert os.path.isdir(dir_path)

def test_create_file(tmp_path):
    file_path = os.path.join(tmp_path, "test.txt")
    create_file(file_path)
    assert os.path.isfile(file_path)

    # Test file creation when the directory doesn't exist
    deep_file_path = os.path.join(tmp_path, "dir", "subdir", "test2.txt")
    create_file(deep_file_path)
    assert os.path.isfile(deep_file_path)

def test_create_directories_from_text(tmp_path):
    structured_tree = """
    root/
        dir1/
            file1.txt
    """

    create_directories_from_text(structured_tree, str(tmp_path))
    assert os.path.exists(os.path.join(tmp_path, "root"))
    assert os.path.exists(os.path.join(tmp_path, "root", "dir1"))
    assert os.path.isfile(os.path.join(tmp_path, "root", "dir1", "file1.txt"))
