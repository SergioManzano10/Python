import zipfile

def extract_archive(archiv_path, dest_dir):
    with zipfile.ZipFile(archiv_path, "r") as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("C:\Users\smanz\OneDrive\Escritorio\PYTHON COURSE\MODULE 1 (PYTHON BASICS)\DAY 17\compressed.zip", "C:\Users\smanz\OneDrive\Escritorio\PYTHON COURSE\MODULE 1 (PYTHON BASICS)\DAY 17")
