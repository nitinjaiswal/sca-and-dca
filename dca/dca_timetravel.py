import os
print(os.path.realpath(__file__))

def copy(file, target):
    with open(file) as fp, open(target, "w") as tp:
        tp.writelines(fp.readlines())

filepath = raw_input("Enter path of the file ")

copy(filepath,".")
