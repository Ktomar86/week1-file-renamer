from pathlib import Path

def list_files(folder_path):
    """Return a list of all files (not folders) inside the given folder."""
    folder = Path(folder_path)
   #files = [f for f in folder.iterdir() if f.is_file()]
    files = []
    for item in folder.iterdir():
        if item.is_file():
            files.append(item)
    return files

def build_new_name(file_path, prefix):
    """Return a new filename with the given prefix added to the front."""
    new_name = prefix + file_path.name
    return new_name

def rename_file(file_path, new_name):
    """Rename a file on disk to new_name. Returns True if successful, False if it failed."""
    try:
        new_path = file_path.parent / new_name
        file_path.rename(new_path)
        return True
    except Exception as error:
        print(f"Could not rename {file_path.name}: {error}")
        return False

if __name__ == "__main__":
    files = list_files("test_folder")

    for f in files:
        new_name = build_new_name(f, "vacation_")
        success = rename_file(f, new_name)
        if success:
            print(f"Renamed {f.name} -> {new_name}")
        

