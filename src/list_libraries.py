import os

def list_libraries():
    libs_dir = os.path.expanduser('~/libs')
    print(f"Listing libraries in {libs_dir}")
    if not os.path.isdir(libs_dir):
        print(f"Directory {libs_dir} does not exist")
        return

    libs = os.listdir(libs_dir)
    print(f"Found {len(libs)} libraries")

    for lib in libs:
        print(lib)

if __name__ == "__main__":
    list_libraries()