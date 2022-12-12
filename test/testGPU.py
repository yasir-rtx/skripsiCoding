from os import system
import tensorflow as tf

system('cls')

if len(tf.config.list_physical_devices('GPU')) > 0:
    gpus = tf.config.list_physical_devices('GPU')                   # assign list gpu to gpus variable
    print("Num GPUs Available: ", len(gpus))                        # print how many gpu available
    for gpu in gpus:
        print("Name:", gpu.name, "  Type:", gpu.device_type)        # print list available gpus
else:
    print("Nothing GPUs Available, you are using CPUs")