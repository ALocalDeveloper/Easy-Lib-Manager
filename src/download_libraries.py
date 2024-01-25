import os
import requests

def download_libraries(urls):
    libs_dir = os.path.expanduser('~/libs')
    if not os.path.isdir(libs_dir):
        os.makedirs(libs_dir)

    for url in urls:
        file_path = os.path.join(libs_dir, url.split('/')[-1])
        if os.path.isfile(file_path):
            print("File already exists.")
            continue

        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response.content)
