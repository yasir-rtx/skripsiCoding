# Import Library
from os.path import exists
from datetime import datetime
import json

# Load Data
mahasiswa_path = "../../Data/mahasiswa.json"
absensi_path = "../../Data/absensi.json"
x = datetime.now()
dates = str(x.day) + "/" + str(x.month) + "/" + str(x.year)

if absensi_path:
    print("absensi.json is ready")
if mahasiswa_path:
    print("mahasiswa.json is ready")
    
###############################################################################################################################
#   Functions
###############################################################################################################################
# Take Attendance
def takeAttendance(nobp):
    # dates="14/12/2022"    # debug fungsi untuk memastikan perubahan hanya terjadi di hari itu
    y = datetime.now()
    times = str(y.hour) + ":" + str(y.minute) + ":" + str(y.second)
    with open(absensi_path, "r") as absensi:
        data = json.load(absensi)
        temp = data[dates]
        
        newData = []
        for mahasiswa in temp:
            # print(mahasiswa)        # dictionary mahasiswa dalam objek date
            for key, value in mahasiswa.items():
                if key == nobp:
                    # print("mahasiswa ditemukan")
                    newData.append(
                        {
                            nobp:{
                                "nobp": value["nobp"],
                                "nama": value["nama"],
                                "date": dates,
                                "time": times,
                                "ket": "Hadir"
                    }})
                else:
                    # print("mahasiswa tidak ditemukan")
                    newData.append(mahasiswa)

    # print(newData)  # debug nilai newdata sebelum di dump
    data.update({dates:newData})
    # print(data)
    json.dump(data, open(absensi_path, "w"), indent=4)
    print(f"{nobp} telah hadir pada {dates}")
###############################################################################################################################

# Ambil absen
nobp = input("nobp: ")
takeAttendance(nobp)