# Specify the file path
file_path = "./files/test.jobname"  # Path i relative to the directory the program i running from (se root path at terminal prompt), in this case you must be placed in the subfolder Path_test
file_path = "./FILES/test.jobname"

# Elements to write to the file
element1 = "FIRST Element"
element2 = "Second Element"

# Write elements to the file
with open(file_path, 'w') as file:
    file.write(element1 + '\n')
    file.write(element2 + '\n')

print(".jobname file created with elements:", element1, element2)
