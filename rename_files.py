from pathlib import Path

def list_files(folder_path):
    """Return a list of all files (not folders) inside the given folder."""
    folder = Path(folder_path)
    files = [f for f in folder.iterdir() if f.is_file()]
    return files

if __name__ == "__main__":
    files = list_files(".")
    for f in files:
        print(f.name)