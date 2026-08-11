def read_file(file_path):
    """Read the contents of a file and return it as a string."""
    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path, content):
    """Write the provided content to a file at the given path."""
    with open(file_path, 'w') as file:
        file.write(content)


def append_to_file(file_path, content):
    """Append the provided content to a file at the given path."""
    with open(file_path, 'a') as file:
        file.write(content)


def list_files_in_directory(directory_path):
    """Return a list of files in the specified directory."""
    import os
    return [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]


def read_json(file_path):
    """Read a JSON file and return its contents as a dictionary."""
    import json
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(file_path, data):
    """Write a dictionary to a JSON file at the given path."""
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)