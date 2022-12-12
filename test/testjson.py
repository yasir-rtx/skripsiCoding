import json
from os import listdir, mkdir
from os.path import isdir, exists

mahasiswa_path = "D:\\College\\Semester 8\\Coding\\Data\\mahasiswa.json"
if not exists(mahasiswa_path):
    with open(mahasiswa_path, "w") as mahasiswa:
        print("File mahasiswa.json is creasted")