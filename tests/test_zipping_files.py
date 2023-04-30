import os
import zipfile
from conftest import PROJECT_RESOURCE_PATH


def test_add_zip_file():
    zip_path = PROJECT_RESOURCE_PATH
    zip_file = 'resources.zip'
    with zipfile.ZipFile(zip_file, 'w') as zip_files:
        for i in os.listdir(zip_path):
            file_path = os.path.join(zip_path, i)
            zip_files.write(file_path, i)

    with zipfile.ZipFile(zip_file, "r") as zip_files:
        for i in os.listdir(zip_path):
            assert i in zip_files.namelist()
