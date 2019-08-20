import os

def list_files(dir):
    """Get all the files in given directory with recursive exploration.
    Return 'None' if the directory does not exist
    
    Arguments:
        dir {string} -- path to directory to get all the files
    
    Returns:
        list -- all the files in given directory
    """
    if os.path.isdir(dir) is False:
        return None

    files = []
    for (dirpath, dirnames, filenames) in os.walk(dir):
        files.extend([os.path.join(dirpath, file) for file in filenames])
    return files