import os
import shutil

def remove_libraries(libs):
    libs_dir = os.path.expanduser('~/libs')

    for lib in libs:
        file_path = os.path.join(libs_dir, lib)

        if os.path.isfile(file_path):
            os.remove(file_path)
            print("Deleted file:", file_path)
        else:
            print("File does not exist:", file_path)

    lib_dir = os.path.join(libs_dir, 'lib')
    if os.path.isdir(lib_dir):
        shutil.rmtree(lib_dir)
        print("Deleted directory:", lib_dir)
    else:
        print("Directory does not exist:", lib_dir)

if __name__ == "__main__":
    libs = input("Enter the names of the libraries you want to remove, separated by spaces: ").split()
    remove_libraries(libs)
