from os import listdir
from random import shuffle
from pathlib import Path
import shutil

from_path = "F:"
to_path = "E:"
files = [f for f in listdir(from_path)]
shuffle(files)

MAX_FILES = 99
n_folder = 1
count_files = len(files)

while len(files) > 0:
    curr_path = to_path + "\\" + str(n_folder)
    Path(curr_path).mkdir(parents=True, exist_ok=True)
    for i in range(min(len(files), MAX_FILES)):
        shutil.copy2(from_path + "\\" + files[0], curr_path)
        files.pop(0)
        print(str(round((count_files - len(files)) / count_files * 100, 1)) + "%")
    n_folder += 1

print("Готово")