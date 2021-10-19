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
