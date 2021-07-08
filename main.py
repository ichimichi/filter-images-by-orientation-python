#!/usr/bin/env python3
import os
import shutil
from PIL import Image
import sys
import pathlib

# dr = sys.argv[1]
# target = sys.argv[2]

dr = os.getcwd()

target = "~/Documents/wallpapers"

target = target[:-1] if target[-1] == "/" else target
target_landscape = target + "/" + "landscape"
target_portrait = target + "/" + "portrait"

try:
    pathlib.Path(target_landscape).mkdir(parents=True, exist_ok=True)
except:
    print("failed to create folders")
    sys.exit(1)

try:
    pathlib.Path(target_portrait).mkdir(parents=True, exist_ok=True)
except:
    print("failed to create folders")
    sys.exit(1)

for f in os.listdir(dr):
    try:
        file = dr + "/" + f
        img = Image.open(file)
        size = img.size
        ratio_portrait = 4 / 3
        ratio = size[0] / size[1]
        ratio_diff = ratio - ratio_portrait
        if ratio_diff < -0.01:
            shutil.copyfile(file, target_portrait + "/" + f)
        else:
            shutil.copyfile(file, target_landscape + "/" + f)
    except (IOError, ValueError):
        pass
