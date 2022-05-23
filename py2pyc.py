import compileall
import os
import shutil

dir_path = '/home/jannat/Documents/FACE_API/ufl_compiled/ufl_ekyc_face_compare_api (copy)'
compileall.compile_dir(dir_path)

pycache_paths = []
sub_dir = [dir_path]

# pycache_paths = pycache_paths + [os.path.join(dir_path, file) for file in os.listdir(dir_path) if '__pycache__' in file]
# print(pycache_paths)
py_file = []
pyc_file = []
pycache_dir = []

while(len(sub_dir)>0):
    parent_dir = sub_dir.pop(0)
    print("parent dir", parent_dir)
    
    py_file = []
    pyc_file = []
    
    for file in os.listdir(parent_dir):
        if 'pycache' in file:
            pycache_dir = os.path.join(parent_dir, file)

            pyc_file = pyc_file + [file for file in os.listdir(pycache_dir)]

        elif os.path.isdir(os.path.join(parent_dir, file)):
            sub_dir.append(os.path.join(parent_dir, file))
        
        if file.endswith(".py"):
            py_file.append(os.path.join(parent_dir, file))

    print("sub_dir", sub_dir)
    print("py_file", py_file)
    print("pycache dir", pycache_dir)
    print("pyc file", pyc_file)
    print()

    if len(py_file) == len(pyc_file) and len(py_file)!=0:
        for pyc in pyc_file:
            pyc_split = pyc.split(".")
            pyc_split[-1] = ".pyc"
            pyc_split.pop(-2)
            
            # renaming
            pyc_newname = "".join(pyc_split)
            print("pyc", pyc)
            print("pyc_newname", pyc_newname)
            os.rename(os.path.join(pycache_dir, pyc), os.path.join(pycache_dir, pyc_newname))

            # moving to prev dir
            # print("moving")
            pyc = os.path.join(pycache_dir, pyc_newname)
            pyc_newname = os.path.join(parent_dir, pyc_newname)
            # print("pyc", pyc)
            # print("pyc newname", pyc_newname)
            shutil.move(pyc, pyc_newname)
        os.rmdir(pycache_dir)

        for py in py_file:
            os.remove(py)

    # print("sub_dir", sub_dir)
    # print("py_file", py_file)
    # print("pycache dir", pycache_dir)
    # print("pyc file", pyc_file)
    # print()

    print()
    print()