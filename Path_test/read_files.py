from pathlib import Path

# Read content from a .jobname file
def read_jobname_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) == 2:
                element1 = lines[0].strip()
                element2 = lines[1].strip()
                return element1, element2
            else:
                print("Invalid .jobname file format. Expected 2 lines.")
                return None, None
    except FileNotFoundError:
        print("File not found:", file_path)
        return None, None

def print_files(files_path):
    # Read and print the content of each .jobname file
    for jobname_file in jobname_files:
        element1, element2 = read_jobname_file(jobname_file)
        if element1 is not None and element2 is not None:
            print("File:", jobname_file)
            print("Element 1:", element1)
            print("Element 2:", element2)
            print()

# Specify the directory path
rel_directory_path = "./FILES/"
abs_directory_path = "C:/Users/peter/OneDrive/Source/Python/PythonFun/Path_test/FiLeS/"

# Use glob to find .jobname files in the relative directory path
jobname_files = Path(rel_directory_path).glob("*.jobname")
print_files(jobname_files)

# Use glob to find .jobname files in the absolute directory path
jobname_files = Path(abs_directory_path).glob("*.jobname")
print_files(jobname_files)


# We can also define our base path and the define the other paths relative to this
WORK_DIR = Path("C:/Users/peter/OneDrive/Source/Python/PythonFun/Path_test/")
FILES_DIR = WORK_DIR / "fIlEs" 
# Use glob to find .jobname files in the absolute directory path
jobname_files = Path(FILES_DIR).glob("*.jobname")
print_files(jobname_files)