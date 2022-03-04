import os
import shutil
source = "C:/Users/Darvis/Desktop/Database/hina/test"
i=0
for root , dir, files in os.walk(source):
    for file in files:
        if file.endswith(".jpg"):
            if os.path.isdir(root+"/"+ "images"):
                path_file = os.path.join(root,file)
                shutil.move(path_file,root+"/"+"images")
            else:
                os.mkdir(root+"/"+"images")
                path_file = os.path.join(root,file)
                shutil.move(path_file,root+"/"+"images")
        if file.endswith(f'{i}'+".zip"):
            if os.path.isdir(root+"/"+f'{i}'+"/"+"annotated"):
                path_file = os.path.join(root,file)
                shutil.move(path_file,root+f'{i}'+"/"+"annotated")
                i=i+1
            else:
                os.mkdir(root+"/"+f'{i}'+"/"+"annotated")
                path_file = os.path.join(root,file)
                shutil.move(path_file,root+"/"+f"{i}"+"/"+"annotated")
                i=i+1
      


