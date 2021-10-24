import serial
import time
import schedule


def get_mass():
    #opens serial connection to arduino
    arduino = serial.Serial('com6', 9600)
    arduino_data = arduino.readline()
    #converts data into int and returns it
    mass = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    #print('arduino input: ' + mass)
    arduino.close()
    return mass


# ----------------------------------------Main Code------------------------------------
# Declare variables to be used

#print('Program started')

# Setting up the Arduino
#get_mass()