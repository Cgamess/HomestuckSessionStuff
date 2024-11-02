from ntypes import jsonsavehandler
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
import modding as modding

moddedsave=r"..\saves\modsave.json"
unmoddedsave=r"..\saves\save.json"

if modding.modded:
    save=moddedsave
else:
    save=unmoddedsave

activesave=jsonsavehandler(save)