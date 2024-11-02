from ntypes import *
import colorama
from collections import deque
from time import perf_counter_ns as pcns
import json
import time
import random
import os
import zipfile
import cryptography as cpty
import gzip
testing=1


files = json.loads(open("..\modfiles.json").read())
moddata=[]
tpmods=[]
mods : list = os.listdir(r".\mods")
modded = bool(mods)
if modded and files:
    for i in mods:
        if i.split(".")[-1] in ["zip64", "zip", "mod", "mod64"]:
            if i.split(".")[-1] in ["zip64", "zip"]:
                if testing:
                    print(f"WARNING: {i.split(".")[-1]} is only for testing/debug, use the correct extenstion (mod, mod64) or it will throw an error")
                else:
                    raise TypeError(f"ERROR: {i.split(".")[-1]} is only for testing/debug, use the correct extenstion (mod, mod64)")
        else:
            if testing:
                raise TypeError(f"ERROR: {i.split(".")[-1]} is invalid, only (zip64, zip, mod, mod64)")
            else:
                raise TypeError(f"ERROR: {i.split(".")[-1]} is invalid, only (mod, mod64)")
    for i in range(len(mods)):
        moddata.append({})
    for i in mods:
        with zipfile.ZipFile(i, 'r') as zip_ref:
            for file_name in files:
                with zip_ref.open(file_name) as file:
                    content = file.read()
                    mods.index(i)[files[file_name][0]]=json.loads(content)
else:
    moddata=[]
    tpmods=[]