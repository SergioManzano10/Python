import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname = filepath.name) # filepath.name extracts the name from the archive but not all the path

# To test if the functin works but it is not necessary
            
if __name__ == "__main__":
    make_archive(filepaths = ["todos.txt", "bonus_example.txt"], dest_dir = "dest")