import serial
import time
import schedule


def get_mass():
    arduino = serial.Serial('com6', 9600)
    arduino_data = arduino.readline()

    mass = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    print('arduino input: {mass}')
    arduino.close()
    return mass


# ----------------------------------------Main Code------------------------------------
# Declare variables to be used


time.sleep(2000)
get_mass()