import os
import requests
import tarfile
import zipfile
from tqdm import tqdm

def download_libraries(urls):
    libs_dir = os.path.expanduser('~/libs')
    if not os.path.isdir(libs_dir):
        os.makedirs(libs_dir)

    for url in urls:
        file_path = os.path.join(libs_dir, url.split('/')[-1])
        if os.path.isfile(file_path):
            print("File already exists.")
            continue

        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

        with open(file_path, 'wb') as f:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()

        if file_path.endswith('.tar.gz'):
            with tarfile.open(file_path, 'r:gz') as tar:
                tar.extractall(path=libs_dir)
        elif file_path.endswith('.zip'):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(path=libs_dir)

        # Remove the downloaded file
        os.remove(file_path)

if __name__ == "__main__":
    urls = input("Enter the URLs of the libraries you want to download, separated by spaces, make sure its the full url: ").split()
    download_libraries(urls)