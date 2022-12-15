# Import Library
from os.path import exists
from datetime import datetime
import json

# Import file dan Path yang dibutuhkan
mahasiswa_path = "../../Data/mahasiswa.json"
absensi_path = "../../Data/absensi.json"
x = datetime.now()
date = str(x.day) + "/" + str(x.month) + "/" + str(x.year)

###############################################################################################################################
#   Functions
###############################################################################################################################
# Generate file absensi.json
def generateAbsensiFile(data):
    print("Generate file : absensi.json")
    with open(absensi_path, "w") as absensi:
        json.dump(data, absensi, indent=4)
    print("File absensi is created\n")
    
# Generate object key(date) into absensi.json
def generateKeyDate(date):
    print(f"Generate key({date})")
    with open(absensi_path, "r") as absensi:
        data = json.load(absensi)
        data.update({date:[]})
        json.dump(data, open(absensi_path, "w"), indent=4)
    print(f"Key({date}) for today is created\n")
    
# Generate objects key(list mahasiswa) into object key(date)
def generateListMahasiswa(date):
    print("Generate Mahasiswa Key")
    with open(mahasiswa_path, "r") as file:
        mahasiswa = json.load(file)
        mahasiswaValue = mahasiswa.values()
        # Generate mahasiswa key into date object in absensi.json
        for value in mahasiswaValue:
            # store nobp value into temporary variable
            nobp = value[0]["nobp"]
            print(f"Generate Mahasiswa Key for {nobp}")
            with open(absensi_path, "r") as absensi:
                # Generate mahasiswa value into date object in absensi.json
                y = {nobp:{
                    "nobp": nobp,
                    "nama": value[0]["nama"],
                    "date": date,
                    "time": "-",
                    "ket": "Tidak Hadir"
                }}
                data = json.load(absensi)
                # metode dump
                temp = data[date]   # akses object hari ini
                temp.append(y)
                json.dump(data, open(absensi_path, "w"), indent=4)
                print(f"Key({nobp}) is generated into object({date})\n")
    print("Mahasiswa Key is generated\n")
###############################################################################################################################

# Prepare absensi.json
if not exists(absensi_path):                                    # create absensi.json
    generateAbsensiFile({})
    generateKeyDate(date)
    generateListMahasiswa(date)
else:                                                           # if absensi.json has been created
    # check if date object is already made or not
    finding = 0
    with open(absensi_path, "r") as absensi:
        data = json.load(absensi)
        dates = data.keys()
        for dateFound in dates:
            if dateFound == date:
                finding = 1
    if finding == 1:                                            # prevent object(date) from being reset
        print("File absensi.json is ready")
    else:                                                       # generate object(date)
        generateKeyDate(date)
        generateListMahasiswa(date)

print("Menu Utama dijalankan\n")