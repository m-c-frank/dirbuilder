import pytest
import dirbuilder.interface

def mock_openai_response_directory_structure():
    class MockResponse:
        def __init__(self):
            self.choices = [{"message": {"content": "root/\n    file1.txt"}}]
    return MockResponse()

def mock_openai_response_subdirectory_structure():
    class MockResponse:
        def __init__(self):
            self.choices = [{"message": {"content": "root/\n    dir1/\n        file2.txt"}}]
    return MockResponse()

def test_generate_directory_structure_single_file(mocker):
    # Mock the OpenAI API response
    mocker.patch('dirbuilder.interface.openai.ChatCompletion.create', return_value=mock_openai_response_directory_structure())

    test_input = """
    root/
        file1.txt
    """
    expected_output = "root/\n    file1.txt"
    result = dirbuilder.interface.generate_directory_structure(test_input)
    assert result == expected_output

def test_generate_directory_structure_subdirectory(mocker):
    # Mock the OpenAI API response for subdirectory structure
    mocker.patch('dirbuilder.interface.openai.ChatCompletion.create', return_value=mock_openai_response_subdirectory_structure())

    test_input = """
    root/
        dir1/
            file2.txt
    """
    expected_output = "root/\n    dir1/\n        file2.txt"
    result = dirbuilder.interface.generate_directory_structure(test_input)
    assert result == expected_output