import pytest

from app.file_utility import list_files

def test_invalid_dir():
    """Invalid directory will yield a None when getting a list of files
    """
    files = list_files('/non-exits-dir')
    assert files == None, "File list is not None"