import os
import sys
req_path=input("Enter the path: ")
if os.path.exists(req_path):
    all_f_ds=[]
else:
    "Please enter Valid Path"
    sys.exit()
if os.path.isfile(req_path):
    print(f"The given path {req_path} is a file. Please pass only directory path")

else:
    all_f_ds=os.listdir(req_path)
    if len(all_f_ds)==0:
        print(f"This given path is {req_path} is empty")
    else:
        req_ex=input("enter the required file extension with . : ")
        req_files=[]
                for each_f in all_f_ds:
            if each_f.endswith(req_ex):
                req_files.append(each_f)
        if len(req_files)==0:
            print(f"There are no {req_ex} files here")
